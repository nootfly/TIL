# python not found


Anyone updating their macOS to Monterey 12.3 will find that they suddenly no longer have the system-provided Python 2.

The reason for this is that Apple removed the system-provided Python 2 installation (details).

So a workaround/solution for this is to use pyenv to install Python 2.7 (or any other specific version you need).

1. Install pyenv with brew to manage different Python versions: brew install pyenv
2. List all installable versions with pyenv install --list
3. Install Python 2.7.18 with pyenv install 2.7.18
4. List installed versions with pyenv versions
5. Set global python version with pyenv global 2.7.18
6. Add eval "$(pyenv init --path)" to ~/.zprofile (or ~/.bash_profile or ~/.zshrc, whichever you need)
7. Relaunch the shell and check that Python works, or run $ source ~/.zprofile (Thanks masoud soroush!)

[https://stackoverflow.com/a/71657414](https://stackoverflow.com/a/71657414)
