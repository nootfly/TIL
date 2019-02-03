# Firebase get IP address function

```javascript

const functions = require('firebase-functions');
const cors = require('cors')({origin: true});

exports.ipAddressFun = functions.https.onRequest((req, res) => {
    return cors(req, res, () => {
  const ipAddress = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
  res.send({ipAddress});
    });
});
```

## Reference

[https://github.com/firebase/functions-samples/blob/master/quickstarts/time-server/functions/index.js](https://github.com/firebase/functions-samples/blob/master/quickstarts/time-server/functions/index.js)

[https://gist.github.com/katowulf/6fffffb45ee5cbfbca6c3511e5d19528](https://gist.github.com/katowulf/6fffffb45ee5cbfbca6c3511e5d19528)