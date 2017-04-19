#iOS common code library

1. add tint color to a button


```swift
    let button = UIButton(frame: aRectHere)
    let buttonImage = UIImage(named: "imageName")
    button.setImage(buttonImage?.withRenderingMode(.alwaysTemplate), for: .normal)
    button.tintColor = .white
```
