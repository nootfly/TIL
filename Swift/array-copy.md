# Copy of an array

```swift
var duplicateArray = originalArray

let x = [NSMutableArray(), NSMutableArray(), NSMutableArray()]
let y = x
let z = x.map { $0.copy() }

var originalArray = [1, 2, 3, 4] as NSArray
var duplicateArray = NSArray(array:originalArray as! [Any], copyItems: true)

```