# run Jupyter in a docker container

1. `sudo chown 1000 hostdir`

2. `docker run -d -p 8888:8888 -v hostdir:/home/jovyan/work jupyter/scipy-notebook`

3. `docker exec -it container_id /bin/bash`

4. Run `jupyter notebook list` to get a url with a token

5. Change the port of the url to the running container's open port and open the url in a browser


Reference:
[https://hub.docker.com/r/jupyter/scipy-notebook/](https://hub.docker.com/r/jupyter/scipy-notebook/)
