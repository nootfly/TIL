# Swift 5 Code snippets

## Add leading padding to view added inside an UIStackView

```swift
stackView.layoutMargins = UIEdgeInsets(top: 0, left: 20, bottom: 0, right: 20)
stackView.isLayoutMarginsRelativeArrangement = true
```

[https://stackoverflow.com/questions/32551890/how-to-add-leading-padding-to-view-added-inside-an-uistackview](https://stackoverflow.com/questions/32551890/how-to-add-leading-padding-to-view-added-inside-an-uistackview)

## Timestamp

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

## Date tomorrow

```swift
extension Date {
    static var yesterday: Date { return Date().dayBefore }
    static var tomorrow:  Date { return Date().dayAfter }
    var dayBefore: Date {
        return Calendar.current.date(byAdding: .day, value: -1, to: noon)!
    }
    var dayAfter: Date {
        return Calendar.current.date(byAdding: .day, value: 1, to: noon)!
    }
    var noon: Date {
        return Calendar.current.date(bySettingHour: 12, minute: 0, second: 0, of: self)!
    }
    var month: Int {
        return Calendar.current.component(.month,  from: self)
    }
    var isLastDayOfMonth: Bool {
        return dayAfter.month != month
    }
}
```

[https://stackoverflow.com/a/44009988](https://stackoverflow.com/a/44009988)

## iOS local notification

```swift
// Notification center property
let userNotificationCenter = UNUserNotificationCenter.current()

func requestNotificationAuthorization() {
    let authOptions = UNAuthorizationOptions.init(arrayLiteral: .alert, .badge, .sound)
    
    self.userNotificationCenter.requestAuthorization(options: authOptions) { (success, error) in
        if let error = error {
            print("Error: ", error)
        }
    }
}

override func viewDidLoad() {
    super.viewDidLoad()
    self.requestNotificationAuthorization()
    self.sendNotification()
}

func sendNotification() {
    let notificationContent = UNMutableNotificationContent()
    notificationContent.title = "Test"
    notificationContent.body = "Test body"
    notificationContent.badge = NSNumber(value: 3)
    
    if let url = Bundle.main.url(forResource: "dune",
                                withExtension: "png") {
        if let attachment = try? UNNotificationAttachment(identifier: "dune",
                                                        url: url,
                                                        options: nil) {
            notificationContent.attachments = [attachment]
        }
    }
    
    let trigger = UNTimeIntervalNotificationTrigger(timeInterval: 5,
                                                    repeats: false)
    let request = UNNotificationRequest(identifier: "testNotification",
                                        content: notificationContent,
                                        trigger: trigger)
    
    userNotificationCenter.add(request) { (error) in
        if let error = error {
            print("Notification Error: ", error)
        }
    }
}

// Local notifications
func application(_ application: UIApplication, didReceive notification: UILocalNotification) {
    UIApplication.shared.applicationIconBadgeNumber = 0
}

// Assing self delegate on userNotificationCenter
self.userNotificationCenter.delegate = self

func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler: @escaping () -> Void) {
    completionHandler()
}

func userNotificationCenter(_ center: UNUserNotificationCenter, willPresent notification: UNNotification, withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
    completionHandler([.alert, .badge, .sound])
}

```

[https://programmingwithswift.com/how-to-send-local-notification-with-swift-5/](https://programmingwithswift.com/how-to-send-local-notification-with-swift-5/)

## Get bandle file path

```swift
let dbUrl = Bundle.main.url(forResource: "myDb", withExtension: "db")!
let dbPath = dbUrl.path
```

## Mark

```swift

// MARK: A mark comment lives here.

// MARK: - A mark comment lives here. A separation line is added.

// MARK: -

```

[https://stackoverflow.com/a/35963262](https://stackoverflow.com/a/35963262)
