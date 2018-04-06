# UIViewController loadView

> If you use Interface Builder to create your views and initialize the view controller, you must not override this method.

>You can override this method in order to create your views manually. If you choose to do so, assign the root view of your view hierarchy to the view property. The views you create should be unique instances and should not be shared with any other view controller object. Your custom implementation of this method should not call super.

Reference:https://developer.apple.com/reference/uikit/uiviewcontroller/1621454-loadview
