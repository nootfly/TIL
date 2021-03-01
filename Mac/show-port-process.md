# Find process locking port on Mac

```sh
netstat -vanp tcp | grep 3000

lsof -i tcp:3000 
sudo lsof -i :3000
kill -9 <PID>
```

[https://stackoverflow.com/a/3855359](https://stackoverflow.com/a/3855359)
