# Using SSH keys inside docker container

## Build command
`docker build -t example --build-arg ssh_prv_key="$(cat ~/.ssh/id_rsa)" --build-arg ssh_pub_key="$(cat ~/.ssh/id_rsa.pub)" --squash .`

## Dockerfile
```yaml

FROM python:3.6-slim

ARG ssh_prv_key
ARG ssh_pub_key

RUN apt-get update && \
    apt-get install -y \
        git \
        openssh-server \
        libmysqlclient-dev

# Authorize SSH Host
RUN mkdir -p /root/.ssh && \
    chmod 0700 /root/.ssh && \
    ssh-keyscan github.com > /root/.ssh/known_hosts

# Add the keys and set permissions
RUN echo "$ssh_prv_key" > /root/.ssh/id_rsa && \
    echo "$ssh_pub_key" > /root/.ssh/id_rsa.pub && \
    chmod 600 /root/.ssh/id_rsa && \
    chmod 600 /root/.ssh/id_rsa.pub

# Avoid cache purge by adding requirements first
ADD ./requirements.txt /app/requirements.txt

WORKDIR /app/

RUN pip install -r requirements.txt

# Remove SSH keys
RUN rm -rf /root/.ssh/

# Add the rest of the files
ADD . .

CMD python manage.py runserver
```

> If you're using Docker 1.13 and have experimental features on you can append --squash to the build command which will merge the layers, removing the SSH keys and hiding them from docker history.

## Reference

[https://stackoverflow.com/a/42125241](https://stackoverflow.com/a/42125241)