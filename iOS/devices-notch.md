# Device type and notch

```swift
if UIDevice().userInterfaceIdiom == .phone {
        switch UIScreen.main.nativeBounds.height {
        case 1136:
            print("iPhone 5 or 5S or 5C")
        case 1334:
            print("iPhone 6/6S/7/8")
        case 1920, 2208:
            print("iPhone 6+/6S+/7+/8+")
        case 2436:
            print("iPhone X, Xs")
        case 2688:
            print("iPhone Xs Max")
        case 1792:
            print("iPhone Xr")
        default:
            print("unknown")
        }
    }

var hasTopNotch: Bool {
if #available(iOS 11.0,  *) {
    return UIApplication.shared.delegate?.window??.safeAreaInsets.top ?? 0 > 20
}
return false
}  
```

## Reference

[Detect if the device is iPhone X](https://stackoverflow.com/questions/46192280/detect-if-the-device-is-iphone-x)