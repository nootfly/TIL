#Watch OS app archive other items issue

When you archive an app which has a watch app, the archived item goes to "Other items".
This issue can be resolved by setting `Skip Install` to `Yes` in the watch app Build Settings. You should archive the app watch from the watch app scheme. Also you can reference [the Apple technique archiving note](https://developer.apple.com/library/content/technotes/tn2215/_index.html#//apple_ref/doc/uid/DTS40011221-CH1-PROJ)
