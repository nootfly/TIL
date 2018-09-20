from os import listdir
from os.path import isfile, join
import os, fnmatch
from datetime import datetime
import re
from collections import defaultdict

global all_files
NAME_CACHE = "name_cache"
all_files = []

class Record(object):
      def __init__(self, filename, name, created = None):
          self.filename = filename
          self.name = name
          self.created = created

      def created_time(self):
          return datetime.fromtimestamp(float(self.created)).strftime('%d %B %Y')

      def __str__(self):
          return "filename={}, name={}, created={}".format(self.filename, self.name, self.created_time())     

def fetch_files(dirname):
    global all_files
    for root, _, files in os.walk(dirname):
       for file in files:
          if file.endswith(".md") and not file.endswith('README.md') and not file.endswith('new.md'):
             filename = os.path.join(root, file)
             stat = os.stat(filename)
             created = None
             try:
                created = stat.st_birthtime
             except AttributeError:
                created = stat.st_mtime
             #print(datetime.fromtimestamp(created).date() == datetime.today().date())
             if (datetime.fromtimestamp(created).date() - datetime.today().date()).days >= 0: 
                  name = open(filename).readline().rstrip().replace('# ', '')
                  record = Record(filename, name, created)
                  all_files.append(record) 

def generate_readme_str():
    text_dict = defaultdict(set)
    for record in all_files:
        temp = '- [{}]({}) - {}\n'.format(record.name, record.filename.replace('./', ''), record.created_time())
        key = re.search('./(.*)/', record.filename).group(1)
        text_dict[key].add(temp)

    return text_dict

def update_readme(text_dict):
    with open("README.md") as f_old, open("new.md", "w") as f_new:
      for line in f_old:
        f_new.write(line)
        for key, texts in text_dict.items():
            if '### ' + key in line:
               for text in texts:
                  f_new.write(text)

def remove_duplicates(text_dict):
    with open("README.md") as f_old:
      for line in f_old:
        for key, texts in text_dict.copy().items():
               for text in texts.copy():
                   if text in line:
                       texts.remove(text)
               if len(text_dict[key]) == 0:
                   del text_dict[key]
            

if __name__ == "__main__":
    fetch_files('.')
    text_dict = generate_readme_str()
    remove_duplicates(text_dict)
    if text_dict:
       update_readme(text_dict)
       os.remove('README.md')
       os.rename("new.md", 'README.md')
              
