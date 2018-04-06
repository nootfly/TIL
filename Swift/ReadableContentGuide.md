# ReadableContentGuide

```swift

    let label = UILabel()
    label.translatesAutoresizingMaskIntoConstraints = false
    label.backgroundColor = UIColor.greenColor()
    label.text = "Hello, World"
    label.sizeToFit()
    view.addSubview(label)

    label.leadingAnchor.constraintEqualToAnchor(
      view.readableContentGuide.leadingAnchor).active = true

    label.topAnchor.constraintEqualToAnchor(
      view.readableContentGuide.topAnchor).active = true

    label.trailingAnchor.constraintEqualToAnchor(
      view.readableContentGuide.trailingAnchor).active = true

    label.bottomAnchor.constraintEqualToAnchor(
      view.readableContentGuide.bottomAnchor).active = true
  ```

  The above examples is from "iOS 9 Swift Programming Cookbook".
