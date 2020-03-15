# All kinds of error handling

## compileswift failed with a nonzero exit code

Xcode version: 11

Solution: Turn off `Parallelize Build` in the scheme settings.

## Xcode 10 Error: Multiple commands produce

Solution: Set CoreData models `Codegen` to `Manual/None`.

[https://stackoverflow.com/a/57763072](https://stackoverflow.com/a/57763072)

## You must provide either a sourceView and sourceRect or a barButtonItem. If this information is not known when you present the alert controller, you may provide it in the UIPopoverPresentationControllerDelegate method -prepareForPopoverPresentation


```swift
if let popoverController = alertController.popoverPresentationController {
    popoverController.barButtonItem = sender
}
self.presentViewController(alertController, animated: true, completion: nil)

//or

if let popoverController = alertController.popoverPresentationController {
    popoverController.sourceView = sender
    popoverController.sourceRect = sender.bounds
}
self.presentViewController(alertController, animated: true, completion: nil)

```

[https://stackoverflow.com/a/26040876](https://stackoverflow.com/a/26040876)