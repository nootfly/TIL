#SDWebImagePrefetcher memory issue

```SDImageCache``` saves images cache in memory by default. If you downloaded lots of images, the app will crash because of low memory.
To solve this issue, we can set ```shouldCacheImagesInMemory``` to ```No```

```objective-c
[SDImageCache sharedImageCache].shouldCacheImagesInMemory = NO;
```
