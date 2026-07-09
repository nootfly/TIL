# Mac developer tools

## 1. Must-have base setup

Install **Xcode** from the App Store or Apple Developer, then install Command Line Tools. Apple provides separate Xcode resources and command line developer tools through Apple Developer downloads. ([Apple Developer][1])

```bash
xcode-select --install
```

Install **Homebrew** first, because it will manage most CLI tools and apps. Homebrew officially supports Apple Silicon Macs and macOS Sonoma or later, with Xcode Command Line Tools installed. ([Homebrew][2])

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then:

```bash
brew update
brew upgrade
```

## 2. Core CLI tools

```bash
brew install git gh wget curl jq yq tree ripgrep fd fzf bat eza zoxide
brew install htop btop watch tmux mas
```

Recommended:

```bash
brew install git-delta
brew install lazygit
brew install starship
```

These make terminal work much nicer:

```bash
brew install --cask iterm2
brew install --cask raycast
brew install --cask rectangle
brew install --cask appcleaner
```

## 3. Shell setup

Use **zsh** with Starship prompt:

```bash
echo 'eval "$(starship init zsh)"' >> ~/.zshrc
```

Useful aliases:

```bash
cat <<'EOF' >> ~/.zshrc

alias ll='eza -la --icons'
alias gs='git status'
alias gc='git commit'
alias gp='git push'
alias gl='git log --oneline --graph --decorate'
alias cat='bat'
alias cd='z'
EOF
```

## 4. iOS / macOS development

Install:

```bash
brew install swiftlint swiftformat xcodegen xcbeautify
brew install --cask xcodes
brew install --cask proxyman
```

I strongly recommend **Xcodes** for managing multiple Xcode versions, especially if you work with iOS beta SDKs.

Also install:

```bash
brew install mint
```

For App Store / CI tooling:

```bash
brew install fastlane
```

## 5. Node.js / web / backend

Use a version manager rather than installing Node directly. Node’s official download page currently lists Node **v24.18.0** as Latest LTS and **v26.4.0** as Latest Release, but for production you should generally stay on LTS. ([Node.js][3])

I’d install **fnm**:

```bash
brew install fnm
echo 'eval "$(fnm env --use-on-cd)"' >> ~/.zshrc
source ~/.zshrc
fnm install --lts
fnm use --lts
```

Then:

```bash
corepack enable
npm install -g pnpm
npm install -g firebase-tools
npm install -g vercel
npm install -g typescript tsx nodemon
```

For API testing:

```bash
brew install --cask postman
brew install --cask bruno
```

## 6. Flutter / Android

Flutter’s official docs provide the current macOS install path and upgrade guidance. ([Flutter Documentation][4])

```bash
brew install --cask flutter
brew install --cask android-studio
```

Then:

```bash
flutter doctor
```

For Android command line tools, install via Android Studio first, then accept licences:

```bash
flutter doctor --android-licenses
```

## 7. Firebase / Google Cloud / AWS / DevOps

```bash
brew install google-cloud-sdk
brew install awscli
brew install terraform
brew install kubectl
brew install k9s
brew install helm
```

For containers:

```bash
brew install --cask docker
```

Alternative if you want lighter local containers:

```bash
brew install colima docker docker-compose
```

For your Firebase/GCP work, I’d definitely install:

```bash
npm install -g firebase-tools
gcloud components install beta
```

## 8. Databases

```bash
brew install postgresql@16
brew install redis
brew install sqlite
brew install mysql-client
```

GUI tools:

```bash
brew install --cask tableplus
brew install --cask db-browser-for-sqlite
```

## 9. AI coding tools

Install these:

```bash
brew install --cask cursor
brew install --cask visual-studio-code
```

Then install CLI tools depending on what you use:

```bash
npm install -g @anthropic-ai/claude-code
npm install -g @openai/codex
```

Also useful:

```bash
brew install aider
```

For Xcode, keep an eye on Apple’s latest Xcode releases because Apple has been adding more AI-assisted coding and agent-style workflow features into Xcode recently. ([TechRadar][5])

## 10. Security / secrets

```bash
brew install gnupg
brew install age
brew install sops
brew install 1password-cli
brew install git-secrets
```

Apps:

```bash
brew install --cask 1password
brew install --cask little-snitch
```

For SSH:

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

## 11. Productivity apps

```bash
brew install --cask notion
brew install --cask obsidian
brew install --cask slack
brew install --cask zoom
brew install --cask microsoft-teams
brew install --cask google-chrome
brew install --cask firefox
```

## My recommended “minimum install” for you

For your actual workflow, I’d start with this:

```bash
brew install git gh jq yq ripgrep fd fzf bat eza zoxide tmux lazygit starship
brew install swiftlint swiftformat xcodegen xcbeautify fastlane
brew install fnm pnpm firebase-tools google-cloud-sdk awscli terraform
brew install docker kubectl k9s helm
brew install postgresql@16 redis sqlite
brew install --cask iterm2 raycast rectangle appcleaner
brew install --cask xcodes cursor visual-studio-code android-studio flutter
brew install --cask docker tableplus proxyman postman 1password
```

## Nice structure for your Mac

Create this folder structure:

```bash
mkdir -p ~/Developer
mkdir -p ~/Developer/work
mkdir -p ~/Developer/personal
mkdir -p ~/Developer/playground
mkdir -p ~/Developer/scripts
mkdir -p ~/.config
```



For your stack, the most important installs are **Xcode, Homebrew, GitHub CLI, Xcodes, fnm/Node LTS, pnpm, Firebase CLI, gcloud, Docker, Cursor, VS Code, Flutter, Android Studio, Proxyman, TablePlus, and 1Password**.

[1]: https://developer.apple.com/xcode/resources/?utm_source=chatgpt.com "Resources - Xcode"
[2]: https://brew.sh/?utm_source=chatgpt.com "Homebrew: The Package Manager for Everywhere"
[3]: https://nodejs.org/en/download?utm_source=chatgpt.com "Download Node.js"
[4]: https://docs.flutter.dev/install?utm_source=chatgpt.com "Install Flutter"
[5]: https://www.techradar.com/pro/apple-launches-xcode-26-3-brings-even-more-ai-power-to-coding-on-mac?utm_source=chatgpt.com "Apple launches Xcode 26.3, brings even more AI power to coding on Mac"
