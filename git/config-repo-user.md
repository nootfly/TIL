# Config Repo user

You can configure an individual repo to use a specific user / email address which overrides the global configuration. From the root of the repo, run

```script
git config user.name "Your Name Here"
git config user.email your@email.com
```

Also you can update `.git/config` file under the repo directory. to add the section below.

```shell
[user]
        name = Your Name Here
        email = your@email.com
```