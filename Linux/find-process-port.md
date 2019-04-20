# Find process locking port 3000

`netstat -vanp tcp | grep 3000`

For `macOS El Capitan` and newer`

`sudo lsof -i tcp:3000`

## Reference

[https://stackoverflow.com/a/3855359](https://stackoverflow.com/a/3855359)