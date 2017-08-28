# run Jupyter in a docker container

1. `docker run -d -P jupyter/scipy-notebook`

2. `docker exec -it container_id /bin/bash`

3. Run `jupyter notebook list` to get a url with a token

4. Change the port of the url to the running container's open port and open the url in a browser
