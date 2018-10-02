# Error Domain=PlugInKit Code=13

When dismissing UIImagePickerViewController on Xcode 10 with Swift 4, you may fix this issue by doing the below:

From Xcode menu open: `Product > Scheme > Edit Scheme` > On your Environment Variables set `OS_ACTIVITY_MODE` in the value set `disable`

## Reference

[https://stackoverflow.com/questions/46608761/picker-error-message-on-exit-encountered-while-discovering-extensions-error-do](https://stackoverflow.com/questions/46608761/picker-error-message-on-exit-encountered-while-discovering-extensions-error-do)