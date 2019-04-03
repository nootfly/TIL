# Deploy an ExpressJs server on AWS lambda using Serverless

1. Create a new project

`sls create --template aws-nodejs --path my-service`

2. Install dependencies

`npm install --save express serverless-http body-parser cors`

3. Create an `index.js`

```javascript
// index.js

const serverless = require('serverless-http');
const express = require('express')
const cors = require('cors');
const app = express()

app.use(require("body-parser").json());
app.use(cors());

app.get('/', function (req, res) {
  res.send('Hello World!')
})

module.exports.handler = serverless(app);
```

4. Update `serverless.yml`

```yaml
# serverless.yml

service: my-express-application

provider:
 name: aws
 runtime: nodejs6.10
 stage: dev
 region: us-east-1

functions:
  app:
    handler: index.handler
    events:
      - http: ANY /
      - http: 'ANY {proxy+}'
```

5. Deploy your function

`sls deploy -d`

## Reference

[https://serverless.com/blog/serverless-express-rest-api/](https://serverless.com/blog/serverless-express-rest-api/)