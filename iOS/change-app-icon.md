# Change app icon

1. Update plist file

```xml
<key>CFBundleIcons</key>
	<dict>
		<key>CFBundleAlternateIcons</key>
		<dict>
			<key>Yalla</key>
			<dict>
				<key>CFBundleIconFiles</key>
				<array>
					<string>Yalla</string>
				</array>
			</dict>
			<key>Yo</key>
			<dict>
				<key>CFBundleIconFiles</key>
				<array>
					<string>Yo</string>
				</array>
			</dict>
		</dict>
		<key>CFBundlePrimaryIcon</key>
		<dict>
			<key>CFBundleIconFiles</key>
			<array>
				<string></string>
			</array>
			<key>UIPrerenderedIcon</key>
			<false/>
		</dict>
	</dict>
```

2. Set alternate icon

```swift
guard let name = name else {
            // Reset to default
            UIApplication.shared.setAlternateIconName(nil)
            return
        }
        
        UIApplication.shared.setAlternateIconName(name){ error in
            if let error = error {
                print(error.localizedDescription)
            }
        }
```

## Reference

[supportsAlternateIcons](https://developer.apple.com/documentation/uikit/uiapplication/2806815-supportsalternateicons)

[Change your app’s icon programmatically in iOS 10.3](https://medium.com/swiftworld/swift-world-change-your-apps-icon-programmatically-in-ios-10-3-8e706a3206b3)
