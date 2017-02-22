# Prepare push notification certificate

1. On the Apple Developer web site, click Member Center, click Certificates, Identifiers and Profiles, and then click Certificates

2. Create development and production SSL push certificate on Apple Development certificate portal, then download the certificates and import them into Keychain Access.

3. Export two private keys as .p12 files from Keychain Access.

4. Generate `.pem` files

   ```
   $ openssl x509 -in cert.cer -inform DER -outform PEM -out cert.pem
$ openssl pkcs12 -in key.p12 -out key.pem -nodes -clcerts
   ```

5. Test certificates:

    ```
    $ openssl s_client -connect gateway.sandbox.push.apple.com:2195 -cert myapnsappcert.pem -key myapnsappprivatekey.pem # sandbox
    $ openssl s_client -connect gateway.push.apple.com:2195 -cert cert.pem -key key.pem # production
    ```


Reference:

https://github.com/node-apn/node-apn/wiki/Preparing-Certificates
http://docs.aws.amazon.com/sns/latest/dg/mobile-push-apns.html
