# Customize iOS share extension UI


1. Create a new UIViewController rather than extending `SLComposeServiceViewController`, and you need to add `@objc (CustomShareViewController)`

   ```swift
   @objc (CustomShareViewController)
   class CustomShareViewController: UIViewController
   ```

2. Create a UI, and remember that you cannot present or show another view controller. If you want to show different UI, you can use `alpha` to show or hide UI elements.

3. Remember to use `extensionContext!.cancelRequest(withError: NSError())` or `extensionContext!.completeRequest(returningItems: [], completionHandler: nil)` to close UI


Reference

http://catthoughts.ghost.io/extensions-in-ios8-custom-views/
http://blog.hellocode.co/post/share-extension/  
