# Serverless function 6 seconds timeout

Serverless set a Lamdba function timeout to 6.00 seconds, If you didn't write timeout statement in serverless.yml.


```yml
# serverless.yml
service: myService

provider:
  name: aws
  runtime: nodejs6.10
  memorySize: 512 # optional, in MB, default is 1024
  timeout: 10 # optional, in seconds, default is 6
  versionFunctions: false # optional, default is true

functions:
  hello:
    handler: handler.hello # required, handler set in AWS Lambda
    name: ${self:provider.stage}-lambdaName # optional, Deployed Lambda name
    description: Description of what the lambda function does # optional, Description to publish to AWS
    runtime: python2.7 # optional overwrite, default is provider runtime
    memorySize: 512 # optional, in MB, default is 1024
    timeout: 10 # optional, in seconds, default is 6
```

Reference: [https://github.com/serverless/serverless/issues/2640](https://github.com/serverless/serverless/issues/2640)

