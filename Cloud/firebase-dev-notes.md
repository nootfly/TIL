# Firebase development notes

## [Incrementing Values Atomically with Cloud Firestore](https://firebase.googleblog.com/2019/03/increment-server-side-cloud-firestore.html)

## [Firebase push ID](https://firebase.googleblog.com/2015/02/the-2120-ways-to-ensure-unique_68.html)

## Deploy to multiple environments

```shell
# add environment
firebase use --add

# Switching environments
firebase use default

firebase deploy -P staging # deploy to staging alias
```

[https://firebase.googleblog.com/2016/07/deploy-to-multiple-environments-with.html](https://firebase.googleblog.com/2016/07/deploy-to-multiple-environments-with.html)
