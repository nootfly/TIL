# Npm behind a corporate web proxy

* Option 1

```shell
export HTTP_PROXY=http://proxyserver:port
export HTTPS_PROXY=http://proxyserver:port

```

* option 2

```shell
npm config set proxy http://proxy.company.com:8080
npm config set https-proxy http://proxy.company.com:8080
```

## Reference

[https://jjasonclark.com/how-to-setup-node-behind-web-proxy/](https://jjasonclark.com/how-to-setup-node-behind-web-proxy/)