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
3. `UIView` `func addConstraint(_ constraint: NSLayoutConstraint)` method
   >When developing for iOS 8.0 or later, set the constraint’s isActive property totrue instead of calling the addConstraint(_:) method directly. The isActive property automatically adds and removes the constraint from the correct view.
