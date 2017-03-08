# UIStackView

 * The UIStackView is a nonrendering subclass of UIView; that is, it does not provide any user interface of its own. Instead, it just manages the position and size of its arranged views. As a result, some properties (like `backgroundColor`) have no effect on the stack view. Similarly, you cannot override layerClass, `draw(_:)`, or `draw(_:in:)`.

* You can also fine tune an arranged view’s appearance by adding additional constraints to the arranged view. For example, you can use constraints to set a minimum or maximum height or width for the view. Or you can define an aspect ratio for the view.

* Be careful to avoid introducing conflicts when adding constraints to views inside a stack view. As a general rule of thumb, if a view’s size defaults back to its intrinsic content size for a given dimension, you can safely add a constraint for that dimension.

* Removing a view from the arrangedSubviews array does not remove it as a subview. The stack view no longer manages the view’s size and position, but the view is still part of the view hierarchy, and is rendered on screen if it is visible.

* Dynamically Changing the Stack View’s Content

  ```swift
  // Animates removing the first item in the stack.
UIView.animateWithDuration(0.25) { () -> Void in
   let firstView = stackView.arrangedSubviews[0]
   firstView.isHidden = true
}
  ```


Reference: https://developer.apple.com/reference/uikit/uistackview
