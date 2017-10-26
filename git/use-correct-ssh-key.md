# Automatically use correct SSH key for remote Git repo

1. In ~/.ssh/ create a file called config with contents based on this:
```
#user1 account
Host github.com-user1
    HostName github.com
    User git
    IdentityFile ~/.ssh/github-user1

#user2 account
Host github.com-user2
    HostName github.com
    User git
    IdentityFile ~/.ssh/github-user2
```

2. `git remote set-url origin git@github.com-user1:user1/your-repo-name.git`

[Automatically use correct SSH key for remote Git repo](https://www.keybits.net/post/automatically-use-correct-ssh-key-for-remote-git-repo/)