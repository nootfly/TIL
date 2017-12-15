# AWS lambda Java read config file

1. Put the config file under `src/main/resources`

2. Read the config file using the code below

```java
InputStream is = WobCredentials.class.getResourceAsStream(serviceAccountPrivateKeyPath);
        String content = convertStreamToString(is);
        JSONObject privateKeyJson = new JSONObject(content);

  String convertStreamToString(java.io.InputStream is) {
        java.util.Scanner s = new java.util.Scanner(is).useDelimiter("\\A");
        return s.hasNext() ? s.next() : "";
    }
```  

Reference: [https://stackoverflow.com/questions/35356200/how-to-load-property-file-from-classpath-in-aws-lambda-java](https://stackoverflow.com/questions/35356200/how-to-load-property-file-from-classpath-in-aws-lambda-java)          
