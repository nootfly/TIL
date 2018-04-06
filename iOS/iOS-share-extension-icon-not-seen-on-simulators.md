# iOS share extension icon not seen on simulators

To solve this issue, two settings are needed to be done.

1. Set `Asset Catalog App Icon Set Name` to `AppIcon` in `Assets.xcassets` in `Build Settings`. `AppIcon` is the app's icon name

2. Select the extension in `AppIcon`'s `File inspector Target Membership`  
