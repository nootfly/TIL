* Silent push notification

You need to push `content-available` in a payload.

  ```json
  {
    "content-available" : 1
  }
  ```
And you can check this in application delegate:

   ```swift
   func application(application: UIApplication, didReceiveRemoteNotification userInfo: [NSObject : AnyObject], fetchCompletionHandler completionHandler: (UIBackgroundFetchResult) -> Void) {
      let aps = userInfo["aps"] as! [String: AnyObject]

    // 1
    if (aps["content-available"] as? NSString)?.integerValue == 1 {
      // Refresh data
      // 2
      let podcastStore = PodcastStore.sharedStore
      podcastStore.refreshItems { didLoadNewItems in
        // 3
        completionHandler(didLoadNewItems ? .NewData : .NoData)
      }
    } else  {
      // News
      // 4
      createNewNewsItem(aps)
      completionHandler(.NewData)
    }
    }
   ```



Reference http://stackoverflow.com/a/36327058/1146834
          https://www.raywenderlich.com/123862/push-notifications-tutorial
