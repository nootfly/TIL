# Nodejs code snippets

## Encrypt and decrypt text

```javascript
// Nodejs encryption with CTR
const crypto = require('crypto');
const algorithm = 'aes-256-cbc';
const key = crypto.randomBytes(32);
const iv = crypto.randomBytes(16);

function encrypt(text) {
 let cipher = crypto.createCipheriv('aes-256-cbc', Buffer.from(key), iv);
 let encrypted = cipher.update(text);
 encrypted = Buffer.concat([encrypted, cipher.final()]);
 return { iv: iv.toString('hex'), encryptedData: encrypted.toString('hex') };
}

function decrypt(text) {
 let iv = Buffer.from(text.iv, 'hex');
 let encryptedText = Buffer.from(text.encryptedData, 'hex');
 let decipher = crypto.createDecipheriv('aes-256-cbc', Buffer.from(key), iv);
 let decrypted = decipher.update(encryptedText);
 decrypted = Buffer.concat([decrypted, decipher.final()]);
 return decrypted.toString();
}

var hw = encrypt("Some serious stuff")
console.log(hw)
console.log(decrypt(hw))
```

[https://codeforgeek.com/encrypt-and-decrypt-data-in-node-js/](https://codeforgeek.com/encrypt-and-decrypt-data-in-node-js/)

## Send emails with attachments using Microsoft graph API

```javascript
exports.sendEmail = (sendTo, subject, message, csvFileName, cvsString) => {

    return new Promise((resolve, reject) => {
        getToken()
            .then((result) => {
                console.log(result.data);
                const attachments = [
                    {
                        "@odata.type": "#microsoft.graph.fileAttachment",
                        name: csvFileName,
                        contentBytes: Buffer.from(cvsString).toString('base64'),
                        contentType: 'text/plain'
                    }
                ];

                const sendData = {
                    message: {
                        subject: subject, body: { contentType: "html", content: message },
                        toRecipients: sendTo.split(',').map(emailAddress => {
                            return { emailAddress: { address: emailAddress.trim() } };
                        })
                        , attachments
                    }, saveToSentItems: false
                };

                const sendConfig = {
                    method: 'POST',
                    url: SEND_URL,
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${result.data.access_token}`
                    },
                    data: sendData
                };
                console.log('sendConfig', sendConfig);

                axios(sendConfig)
                    .then(() => {
                        resolve();
                    })
                    .catch(err => {
                        console.log("get token error", err);
                        reject(err);
                    });

            })
            .catch(err => {
                console.log("get token error", err);
                reject(err);
            });
    });

};
```
