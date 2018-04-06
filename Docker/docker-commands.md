# docker commands

* run a ubuntu image

   `docker run -i -t ubuntu /bin/bash`

* go into a running container

    `docker exec -i -t containerName /bin/bash`

* resolve "The default lines below are for a sh/bash shell, you can specify the shell you're using, with the --shell flag." error to use this command

    `eval $(docker-machine env docker-sandbox --shell bash)`

* create a volume

   `docker run --name mysites -v /Users/noot/docker/data:/data -it nootfly/docker1.1.2`

* commit a container

   `docker commit 1ff9c95fdc30 nootfly/docker1.1.2`

* docker-machine configures at the start of each shell session

  `eval $(docker-machine env docker-sandbox)`

* docker saves an image to a tar

   `docker save -o ~/container1.tar container1`

* docker recovery an image from a tar

   `docker load -i /root/container1.tar`

* rename docker container

   `docker rename CONTAINER NEW_NAME`

* copy files from the container to the host  

   `docker cp <containerId>:/file/path/within/container /host/path/target`

* [Removing Docker containers and images](https://zaiste.net/posts/removing_docker_containers/)    
