# Web prototype tools

## [Netlify](https://www.netlify.com)

> Netlify lets you link a GitHub, GitLab, or Bitbucket repository to a site. Each time you push to your Git provider, Netlify runs a build with your tool of choice and deploys the result to our powerful CDN.

## [ngrok](https://ngrok.com/)

> ngrok allows you to expose a web server running on your local machine to the internet. Just tell ngrok what port your web server is listening on.

1. Download ngrok and connect to your account
2. Run `ngrok http 3000` to expose a local webserver

## [surge.sh](https://surge.sh)

> run surge from within any directory, to publish that directory onto the web.

```script
sudo npm install --global surge

surge build/

```

## [now.sh](https://surge.sh)

[How to Deploy Express on Now.sh](https://dev.to/warenix/how-to-deploy-express-on-nowsh-414i)

1 . Add `now.json` in your ExpressJs project dirctory

```json
{
  "version": 2,
  "builds": [{ "src": "server.js", "use": "@now/node-server" }],
"routes": [{
    "headers": {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "X-Requested-With, Content-Type, Accept"
    },
    "src": "/.*",
    "dest": "/server.js"
}]
}
```

2. Run `now` to deploy your app

## [ExpressJs on AWS lambda](../Cloud/aws-lambda-express-server.md)

## [Heroku](https://www.heroku.com)

>  * Instant Deployment with Git push - build of your application is performed by Heroku using your build scripts

> * Plenty of Add-on resources (applications, databases etc.)
> * Processes scaling - independent scaling for each component of your app without affecting functionality and performance
> * Isolation - each process (aka dyno) is completely isolated from each other
> * Full Logging and Visibility - easy access to all logging output from every component of your app and each process (dyno)

[https://stackoverflow.com/a/14081822](https://stackoverflow.com/a/14081822)

## Static websites on Amamzon S3

   ### manual steps:

   1. Create a S3 bucket and set it as a public static website

   2. Upload your html files to the S3 bucket

   3. Create a SSL certificate in AWS certificate mananger

   4. Create a AWS CloudFront to point to the S3 bucket and use the SSL certificate

   5. Create an A record in AWS Route53 to point to the CloudFront point


