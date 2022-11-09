# E: List directory /var/lib/apt/lists/partial is missing.


```docker
FROM jupyter/scipy-notebook

RUN pip install mlflow
RUN pip install sklearn

USER root
RUN apt-get update && apt-get install -y curl
USER jovyan
```