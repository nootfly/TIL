# Docker nginx log configuration

If you use ```nginx``` docker offical image, the nginx logs point to ```stderr``` and ```stdout```. You need to keep logs into different files, otherwise the logs won't be saved. For example:

```
http {
  access_log /var/log/nginx/access1.log;
  error_log /var/log/nginx/error1.log;
}
```
