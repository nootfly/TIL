# Swift Code snippets

## add leading padding to view added inside an UIStackView

```swift
stackView.layoutMargins = UIEdgeInsets(top: 0, left: 20, bottom: 0, right: 20)
stackView.isLayoutMarginsRelativeArrangement = true
```

[https://stackoverflow.com/questions/32551890/how-to-add-leading-padding-to-view-added-inside-an-uistackview](https://stackoverflow.com/questions/32551890/how-to-add-leading-padding-to-view-added-inside-an-uistackview)

## timestamp

```swift
// current date and time
let someDate = Date()

// time interval since 1970
let myTimeStamp = someDate.timeIntervalSince1970
```

## Change year in Date

```swift
var component = calendar.dateComponents([.year, .month, .day, .hour, .minute, .second], from: base)
component.year = year
Calendar.current.date(from: component)
```

[https://dev.to/onmyway133/changing-year-in-date-in-swift](https://dev.to/onmyway133/changing-year-in-date-in-swift)
