# Manage different docker versions

When you try to manage different docker container using docker-machine, it is impossible to manage them on one machine as those docker demons may have different docker versions. One solution is to use one docker container to manage one docker version containers.

1. Get a docker container from docker hub

    `docker run --name mysites  -it nootfly/ubuntu_docker`

2. Install specific version docker:[Reference](https://docs.docker.com/engine/installation/linux/ubuntulinux/)

    `sudo apt-get install docker-engine=1.12.0-0~xenial`
