# Upgrade Swift 3 to Swift 4

```swift
//swift 3
let avaData = UIImageJPEGRepresentation(avaImg.image!, 0.5) 
NotificationCenter.default.addObserver(forName: .UIApplicationDidBecomeActive, object: nil, queue: nil) { _ in /* some code */ }

//swift 4.2
yourImageObject.jpegData(compressionQuality: 0.5)
NotificationCenter.default.addObserver(forName: UIApplication.didBecomeActiveNotification, object: nil, queue: nil) { _ in /* some code */ }
```