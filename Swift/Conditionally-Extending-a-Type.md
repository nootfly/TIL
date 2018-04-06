# Conditionally Extending a Type

Conform to the OptionSetType protocol

```swift
extension SequenceType where
  Generator.Element : IntegerArithmeticType{
  public func canFind(value: Generator.Element) -> Bool{
    for (_, v) in self.enumerate(){
      if v == value{
        return true
      }
    }
    return false
  }
}
```

You can use it like so:

```swift
func example1(){

    if [1, 3, 5, 7].canFind(5){
      print("Found it")
    } else {
      print("Could not find it")
    }

  }
 ```

 The above examples are from "iOS 9 Swift Programming Cookbook".
