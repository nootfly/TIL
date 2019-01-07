# Notification callback function for Safari

```javascript
try {
        Notification.requestPermission()
            .then(() => doSomething())
    } catch (error) {
        // Safari doesn't return a promise for requestPermissions and it
        // throws a TypeError. It takes a callback as the first argument
        // instead.
        if (error instanceof TypeError) {
            Notification.requestPermission(() => {
                doSomething();
            });
        } else {
            throw error;
        }
    }
```

## Reference

[https://stackoverflow.com/a/39282539](https://stackoverflow.com/a/39282539)