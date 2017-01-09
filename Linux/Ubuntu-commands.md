# Ubuntu commands

* Check ubuntu version
  If `lsb_release -a` does not work, you can use `cat /etc/*-release`.

* create ssh keys
  `ssh-keygen -t rsa`

* Upgrade git version (http://askubuntu.com/questions/568591/how-do-i-install-the-latest-version-of-git-with-apt)

```
sudo apt-add-repository ppa:git-core/ppa
sudo apt-get update
sudo apt-get install git
```
