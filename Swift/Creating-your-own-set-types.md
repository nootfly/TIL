# Creating your own set types

Conform to the OptionSetType protocol

```swift
struct IphoneModels : OptionSetType, CustomDebugStringConvertible{

    let rawValue: Int
    init(rawValue: Int){
      self.rawValue = rawValue
    }

    static let Six = IphoneModels(rawValue: 0)
    static let SixPlus = IphoneModels(rawValue: 1)
    static let Five = IphoneModels(rawValue: 2)
    static let FiveS = IphoneModels(rawValue: 3)

    var debugDescription: String{
      switch self{
      case IphoneModels.Six:
        return "iPhone 6"
      case IphoneModels.SixPlus:
        return "iPhone 6+"
      case IphoneModels.Five:
        return "iPhone 5"
      case IphoneModels.FiveS:
        return "iPhone 5s"
      default:
        return "Unknown iPhone"
      }
    }
  }
```

You can use it like so:

```swift
func example1(){

   let myIphones: [IphoneModels] = [.Six, .SixPlus]

   if myIphones.contains(.FiveS){
     print("You own an iPhone 5s")
   } else {
     print("You don't seem to have an iPhone 5s but you have these:")
     for i in myIphones{
       print(i)
     }
   }
 }
 ```

 The above examples are from "iOS 9 Swift Programming Cookbook".
