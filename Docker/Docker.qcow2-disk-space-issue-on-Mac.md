# Docker.qcow2 disk space issue on Mac

I found `Docker.qcow2` uses 28G on my mac. I solve this issue using the commands below.

```script
     docker rm $(docker ps -a -q)
     docker rmi $(docker images -q)
     docker volume rm $(docker volume ls |awk '{print $2}')
     rm -rf ~/Library/Containers/com.docker.docker/Data/*
```

Reference: [https://github.com/docker/for-mac/issues/371](https://github.com/docker/for-mac/issues/371)
