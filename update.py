import os
import re
import subprocess
from datetime import datetime
from collections import defaultdict

DIR_TO_HEADER = {
    'raspberrypi': 'Raspberry',
    'javascript': 'Javascript',
    'reactnative': 'ReactNative',
    'watchos': 'WatchOS',
    'ios': 'iOS',
}

EXCLUDE_DIRS = {'.git', '.vscode', 'images', '.github'}

def get_header_name(dir_name):
    lower_dir = dir_name.lower()
    if lower_dir in DIR_TO_HEADER:
        return DIR_TO_HEADER[lower_dir]
    return dir_name.capitalize()

def get_git_creation_date(filepath):
    try:
        result = subprocess.run(
            ['git', 'log', '--follow', '--format=%aI', '--', filepath],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        dates = [d.strip() for d in result.stdout.strip().split('\n') if d.strip()]
        if dates:
            iso_date = dates[-1] # Oldest date is the last one in --follow
            dt = datetime.fromisoformat(iso_date)
            return dt.strftime('%d %B %Y')
    except Exception:
        pass
    return None

def get_file_title(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('#'):
                    return re.sub(r'^#+\s*', '', line)
    except Exception:
        pass
    return os.path.splitext(os.path.basename(filepath))[0]

def main():
    # 1. Scan filesystem for all .md files (excluding README.md, etc.)
    all_md_files = []
    for root, dirs, files in os.walk('.'):
        # Exclude directories in-place
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            if file.endswith('.md') and file not in ('README.md', '2026.md', 'new.md'):
                filepath = os.path.join(root, file)
                # Normalize path (e.g. ./Linux/tmux.md -> Linux/tmux.md)
                rel_path = os.path.relpath(filepath, '.')
                all_md_files.append((filepath, rel_path))

    # 2. Parse current README.md to find already indexed files
    already_indexed = set()
    posts_by_path = {}
    
    # We want to read README.md if it exists
    current_category = None
    readme_pattern = re.compile(r'^\s*-\s*\[(.*?)\]\((.*?\.md)\)(?:\s*-\s*(.*))?$')
    
    if os.path.exists('README.md'):
        with open('README.md', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('### '):
                    current_category = line.replace('### ', '').strip()
                match = readme_pattern.match(line)
                if match:
                    title, path, date = match.groups()
                    already_indexed.add(path)
                    if path not in posts_by_path:
                        posts_by_path[path] = {
                            'path': path,
                            'title': title,
                            'date': date or '',
                            'category': current_category or 'Others'
                        }

    # 3. Process new files
    new_posts = []
    today_str = datetime.today().strftime('%d %B %Y')
    
    for filepath, rel_path in all_md_files:
        if rel_path not in already_indexed:
            # Determine category, title, date
            parts = rel_path.split(os.sep)
            if len(parts) > 1:
                category_dir = parts[0]
                category = get_header_name(category_dir)
            else:
                category = 'Others'
            
            title = get_file_title(filepath)
            date = get_git_creation_date(filepath) or today_str
            
            post = {
                'path': rel_path,
                'title': title,
                'date': date,
                'category': category
            }
            new_posts.append(post)
            posts_by_path[rel_path] = post

    # Group new posts by category
    new_posts_by_category = defaultdict(list)
    for post in new_posts:
        new_posts_by_category[post['category']].append(post)

    # 4. Update README.md
    if new_posts:
        temp_readme_path = 'README.md.tmp'
        updated = False
        with open('README.md', 'r', encoding='utf-8') as f_old, open(temp_readme_path, 'w', encoding='utf-8') as f_new:
            for line in f_old:
                f_new.write(line)
                # Check if this line is a category header
                clean_line = line.strip()
                if clean_line.startswith('### '):
                    cat_name = clean_line.replace('### ', '').strip()
                    # If we have new posts for this category, append them immediately after the header line
                    if cat_name in new_posts_by_category:
                        for post in new_posts_by_category[cat_name]:
                            f_new.write(f'- [{post["title"]}]({post["path"]}) - {post["date"]}\n')
                        # Clear it so we don't write again (in case of duplicate headers)
                        del new_posts_by_category[cat_name]
                        updated = True
        
        # Replace old README.md with updated one
        if updated:
            os.replace(temp_readme_path, 'README.md')
        else:
            if os.path.exists(temp_readme_path):
                os.remove(temp_readme_path)

    print("Successfully updated README.md.")

if __name__ == '__main__':
    main()
