# github auto push script

1. Create ssh key and add the public key to your github repository

`ssh-keygen -t rsa`

2. Create a script to commit changes and push it to the remote github server.

```shell
#!/bin/bash

MESSAGE="Update"
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
else
  MESSAGE=$1
fi
cd /data/myFiles/github/TIL/
git add . && git commit -m $MESSAGE && git push origin master
```
