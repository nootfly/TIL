# Run Tomcat image


```
docker run -d --rm -p 8888:8080 -v /Users/noot/tomcat/conf:/usr/local/tomcat/conf -v /Users/noot/tomcat/webapps:/usr/local/tomcat/webapps tomcat:8.5.29-jre9
```