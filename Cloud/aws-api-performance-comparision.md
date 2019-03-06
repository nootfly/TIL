# AWS API performance comparision

> Do you need high performance? Using dedicated instances with Fargate (or ECS/EKS/EC2) is your best best. This will require more setup and infrastructure management, but that may be necessary for your use case.

> Is your business logic limited? If so, use API Gateway service proxy. API Gateway service proxy is a performant, low-maintenance way to stand up endpoints and forward data to another AWS service.

>In the vast number of other situations, use AWS Lambda. Lambda is dead-simple to deploy (if you’re using a deployment tool). It’s reliable and scalable. You don’t have to worry about tuning a bunch of knobs to get solid performance. And it’s code, so you can do anything you want. I use it for almost everything.

## Reference
[AWS API Performance Comparison: Serverless vs. Containers vs. API Gateway integration](https://www.alexdebrie.com/posts/aws-api-performance-comparison/)