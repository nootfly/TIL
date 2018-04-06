#PODS_ROOT issue

I run into the issue below. It did not work even I run `Pod install`. The solution to this issue was that I
installed a new version CocoaPods.

```
diff: /../Podfile.lock: No such file or directory
diff: /Manifest.lock: No such file or directory
error: The sandbox is not in sync with the Podfile.lock. Run 'pod install' or update your CocoaPods installation.
```
