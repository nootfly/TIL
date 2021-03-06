# UILayoutGuide

>The UILayoutGuide class is designed to perform all the tasks previously performed by dummy views, but to do it in a safer, more efficient manner. Layout guides do not define a new view. They do not participate in the view hierarchy. Instead, they simply define a rectangular region in their owning view’s coordinate system that can interact with Auto Layout.


## Creating Layout Guides

>To create a layout guide, you must perform the following steps:
1. Instantiate a new layout guide.
2. Add the layout guide to a view by calling the view’s `addLayoutGuide(_:)` method.
3. Define the position and size of the layout guide using Auto Layout.

>You can use these guides to define the space between elements in your layout. The following example shows layout guides used to define an equal spacing between a series of views.

  ```swift
      let space1 = UILayoutGuide()
      view.addLayoutGuide(space1)

      let space2 = UILayoutGuide()
      view.addLayoutGuide(space2)

      space1.widthAnchor.constraint(equalTo: space2.widthAnchor).isActive = true
      saveButton.trailingAnchor.constraint(equalTo: space1.leadingAnchor).isActive = true
      cancelButton.leadingAnchor.constraint(equalTo: space1.trailingAnchor).isActive = true
      cancelButton.trailingAnchor.constraint(equalTo: space2.leadingAnchor).isActive = true
      clearButton.leadingAnchor.constraint(equalTo: space2.trailingAnchor).isActive = true
  ```



Reference: https://developer.apple.com/reference/uikit/uilayoutguide   
