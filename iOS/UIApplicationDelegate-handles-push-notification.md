# UIApplicationDelegate handles push notification

* If your app wasn’t running and the user launches it by tapping the push notification, the push notification is passed to your app in the launchOptions of `application(_:didFinishLaunchingWithOptions:)`.

* If your app was running and in the foreground, the push notification will not be shown, but `application(_:didReceiveRemoteNotification:)` will be called immediately.

* If your app was running or suspended in the background and the user brings it to the foreground by tapping the push notification, `application(_:didReceiveRemoteNotification:)` will be called.
