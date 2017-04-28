#iOS common code library

1. add tint color to a button


```swift
    let button = UIButton(frame: aRectHere)
    let buttonImage = UIImage(named: "imageName")
    button.setImage(buttonImage?.withRenderingMode(.alwaysTemplate), for: .normal)
    button.tintColor = .white
```

2. Add `Mark` to Swift code

   ```swift
     //MARK: viewDidLoad
     //TODO: - viewDidLoad
     //FIXME - viewDidLoad

   ```
