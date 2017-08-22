#Swift 3 cheat sheet

1. Empty Strings
```swift
var anEmptyString = ""
var anotherEmptyString = String()
if anEmptyString.isEmpty {
print("String is empty")
 }
```

2. stride functions
```
let fourToTwo = Array(stride(from: 4, to: 1, by: -1)) // [4, 3, 2]
let fourToOne = Array(stride(from:4, through: 1, by: -1)) // [4, 3, 2, 1]
```
3. Mutable parameters are not favorable in Swift functional programming and are removed from Swift 3.0. Functions can have inout parameters.
```
func swapTwoInts( a: inout Int, b: inout Int) {
    let temporaryA = a
    a = b
    b = temporaryA
}
```
4. nested functions
```
func returnTwenty() -> Int {
    var y = 10
    func add() {
        y += 10
    }
    add()
    return y
}

 returnTwenty()
```
5. AnyObject can represent an instance of any class type. Any can represent an instance of any type, including structs, enumerations, and function types.
6. Swift enables us to declare nested types whereby we nest supporting enumerations, classes, and structures within the definition of the type that they support. 
7.
