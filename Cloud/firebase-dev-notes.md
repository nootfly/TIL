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

## test functions using shell

```shell
firebase experimental:functions:shell

//firebase > aggregateCustomers({})
```

[https://firebase.googleblog.com/2017/09/testing-functions-locally-with-cloud.html](https://firebase.googleblog.com/2017/09/testing-functions-locally-with-cloud.html)

## firebase functions partially deployed

```shell
firebase deploy --only functions:makeUppercase
```

[https://stackoverflow.com/a/44492787](https://stackoverflow.com/a/44492787)

## firebase `Deadline Exceeded` error

```javascript
let ref = db.collection("orders");

return new Promise((resolve, reject) => {
            ref.add(order).then((order) => {
                logger.info(order);
                resolve(order);
            }).catch((err) => {
                logger.info(err);
                reject(err);
            })
})
```

## Refresh token

```javascript
firebase.auth().currentUser.getIdToken(/ forceRefresh / true)
.then(function(idToken) {

}).catch(function(error) {

});
```

[https://stackoverflow.com/a/38233818](https://stackoverflow.com/a/38233818)

[https://medium.com/@jwngr/implementing-firebase-auth-session-durations-82fa7b1fff08](https://medium.com/@jwngr/implementing-firebase-auth-session-durations-82fa7b1fff08)

## deploy firestore rules

```shell
# Deploy your .rules file
firebase deploy --only firestore:rules
```

[https://firebase.google.com/docs/rules/manage-deploy](https://firebase.google.com/docs/rules/manage-deploy)

## function region

```
lazy var functions = Functions.functions(region: "europe-west1")
```


