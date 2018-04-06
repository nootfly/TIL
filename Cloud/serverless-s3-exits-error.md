# Serverless S3 bucket exists error

To solve this issue there are two steps:

1. remove s3 reference from events
2. add CORS configruation as below:

   ```yaml
     resources:
       Resources:
         S3BucketMyBucket:
           Type: AWS::S3::Bucket
           Properties:
             BucketName: bucketname-${self:provider.stage}
             CorsConfiguration:
               CorsRules:
                 - AllowedHeaders:
                     - "*"
                   AllowedMethods:
                     - GET
                     - POST
                     - PUT
                   AllowedOrigins:
                     - "*"
   ```
