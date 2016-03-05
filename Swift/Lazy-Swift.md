#Lazy Swift


```lazy var``` and ```LazySequence``` examples are as the blow. The code is from http://alisoftware.github.io/swift/2016/02/28/being-lazy/?utm_campaign=iOS%2BDev%2BWeekly&utm_medium=web&utm_source=iOS_Dev_Weekly_Issue_240

```
class Avatar {
  static let defaultSmallSize = CGSize(width: 64, height: 64)

  lazy var smallImage: UIImage = {
    let size = CGSize(
      width: min(Avatar.defaultSmallSize.width, self.largeImage.size.width),
      height: min(Avatar.defaultSmallSize.height, self.largeImage.size.height)
    )
    return self.largeImage.resizedTo(size)
  }()
  var largeImage: UIImage

  init(largeImage: UIImage) {
    self.largeImage = largeImage
  }
}
```

```
let array = Array(0..<1000)
let incArray = array.lazy.map(increment)
print("Result:")
print(incArray[0], incArray[4])
```
