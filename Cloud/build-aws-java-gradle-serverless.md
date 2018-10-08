# Build AWS Java lambda Serverless

1. Create a project

   `sls create --template aws-java-gradle --path autoreply`
2. Build the project

   `./gradlew build`
3. Deploy the project

   `sls deploy -v`