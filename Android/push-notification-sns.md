# Android FCM and AWS SNS settings

1. Add a new android project to Firebase console, and go to the project settings to add a server key and download `google-services.json`. The server key is for AWS SNS android application API key.

2. Add `google-services.json` to the Android project app folder, and follow [this guide](https://firebase.google.com/docs/cloud-messaging/android/client) to setup Firebase and FCM SDK

3. You can use Postman to test `push notification` following [this article](https://medium.com/android-school/test-fcm-notification-with-postman-f91ba08aacc3)

4. The `gotcha part` is about AWS SNS JSON template which uses `data`. But `notification` should be used in the JSON file. Check [this answer](https://stackoverflow.com/questions/38300450/fcm-with-aws-sns?answertab=active#tab-top) on Stackoverflow.