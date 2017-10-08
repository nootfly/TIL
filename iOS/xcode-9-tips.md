# Xcode 9 tips

* press the `Cmd+Ctrl+E` buttons to rename

* `Cmd+Ctrl+left mouse button` or `Cmd+Ctrl+J` or `Cmd+Right mouse click` to jump to definition

*  `.xcodesamplecode.plist` is what triggers Xcode to render the Markdown as seen in their sample. This file can be found under the `.xcodeproj` (within Package Contents). The content of this file is as the below. Reference:[https://dev.to/danielinoa_/rendering-markdown-in-xcode-9](https://dev.to/danielinoa_/rendering-markdown-in-xcode-9)

```
 <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
  <plist version="1.0">
  <array/>
  </plist>
```

* The Main Thread Checker is a standalone tool for Swift and C languages that detects invalid usage of AppKit, UIKit, and other APIs on a background thread.