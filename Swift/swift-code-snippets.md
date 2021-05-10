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

## Save photo to album

```swift
UIImageWriteToSavedPhotosAlbum(yourImage, self, #selector(image(_:didFinishSavingWithError:contextInfo:)), nil)


@objc func image(_ image: UIImage, didFinishSavingWithError error: NSError?, contextInfo: UnsafeRawPointer) {
    if let error = error {
        // we got back an error!
        let ac = UIAlertController(title: "Save error", message: error.localizedDescription, preferredStyle: .alert)
        ac.addAction(UIAlertAction(title: "OK", style: .default))
        present(ac, animated: true)
    } else {
        let ac = UIAlertController(title: "Saved!", message: "Your altered image has been saved to your photos.", preferredStyle: .alert)
        ac.addAction(UIAlertAction(title: "OK", style: .default))
        present(ac, animated: true)
    }
}
```

[https://www.hackingwithswift.com/example-code/media/uiimagewritetosavedphotosalbum-how-to-write-to-the-ios-photo-album](https://www.hackingwithswift.com/example-code/media/uiimagewritetosavedphotosalbum-how-to-write-to-the-ios-photo-album)

## Copy text to the clipboard

```swift
let pasteboard = UIPasteboard.general
pasteboard.string = "Hello, world!"

if let string = pasteboard.string {
    // text was found and placed in the "string" constant
}
```

[https://www.hackingwithswift.com/example-code/system/how-to-copy-text-to-the-clipboard-using-uipasteboard](https://www.hackingwithswift.com/example-code/system/how-to-copy-text-to-the-clipboard-using-uipasteboard)

## Get configuration from PLIST

```swift
// Environment.swift

import Foundation

public enum Environment {
  // MARK: - Keys
  enum Keys {
    enum Plist {
      static let rootURL = "ROOT_URL"
      static let apiKey = "API_KEY"
    }
  }

  // MARK: - Plist
  private static let infoDictionary: [String: Any] = {
    guard let dict = Bundle.main.infoDictionary else {
      fatalError("Plist file not found")
    }
    return dict
  }()

  // MARK: - Plist values
  static let rootURL: URL = {
    guard let rootURLstring = Environment.infoDictionary[Keys.Plist.rootURL] as? String else {
      fatalError("Root URL not set in plist for this environment")
    }
    guard let url = URL(string: rootURLstring) else {
      fatalError("Root URL is invalid")
    }
    return url
  }()

  static let apiKey: String = {
    guard let apiKey = Environment.infoDictionary[Keys.Plist.apiKey] as? String else {
      fatalError("API Key not set in plist for this environment")
    }
    return apiKey
  }()
}
```

[https://thoughtbot.com/blog/let-s-setup-your-ios-environments](https://thoughtbot.com/blog/let-s-setup-your-ios-environments)

## WatchOS update complications

```swift
        let server = CLKComplicationServer.sharedInstance()
        for complication in server.activeComplications ?? [] {
                server.reloadTimeline(for: complication)

        }
```

## SFSafariViewController reader mode

```swift
let urlString = "http://www.google.com"
let url = URL(string: urlString)!
let config = SFSafariViewController.Configuration()
config.entersReaderIfAvailable = true
let safariVC = SFSafariViewController(url: url, configuration: config)
present(safariVC, animated: true, completion: nil)
```

[https://stackoverflow.com/a/49107463](https://stackoverflow.com/a/49107463)

## Change default global tint color

```swift
@UIApplicationMain class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func application(application: UIApplication!, didFinishLaunchingWithOptions launchOptions: NSDictionary!) -> Bool {

        self.window = UIWindow(frame: UIScreen.mainScreen().bounds)

        // ...

        self.window!.tintColor = UIColor.orangeColor()

        return true
    }
}
```

[https://stackoverflow.com/a/25095089](https://stackoverflow.com/a/25095089)

## simulator sqlite db paths

```swift
let dirPaths = NSSearchPathForDirectoriesInDomains(.DocumentDirectory, .UserDomainMask, true)
var docsDir = dirPaths[0]

print(docsDir)

// use app grpup

public lazy var applicationDocumentsDirectory: URL? = {
        // The directory the applicatio:  uses to store the Core Data store file. This code uses a directory named "com.nootapp.CoreDataTest" in the application's documents Application Support directory
        return FileManager.default.containerURL(forSecurityApplicationGroupIdentifier: "group.com.appgroup")
}()

guard let storeURL = self.applicationDocumentsDirectory?.appendingPathComponent("CoreData.sqlite") else {
            fatalError("Could not get sqlite url.")
        }

Swift.debugPrint("storeURL", storeURL.absoluteString)
```

## check iCloud login

```swift
if FileManager.default.ubiquityIdentityToken != nil {
    print("iCloud Available")
} else {
    print("iCloud Unavailable")
}
```

[https://stackoverflow.com/a/39053572](https://stackoverflow.com/a/39053572)

## display base64 string image

```swift
if let imageData = Data.init(base64Encoded: base64String) {
imageView.image = UIImage(data: imageData)
}
```

## SF symbols

[https://www.avanderlee.com/swift/sf-symbols-guide/](https://www.avanderlee.com/swift/sf-symbols-guide/)

## hide files

```swift
extension URL {
    /// `true` is hidden (invisible) or `false` is not hidden (visible)
    var isHidden: Bool {
        get {
            return (try? resourceValues(forKeys: [.isHiddenKey]))?.isHidden == true
        }
        set {
            var resourceValues = URLResourceValues()
            resourceValues.isHidden = newValue
            do {
                try setResourceValues(resourceValues)
            } catch {
                print("isHidden error:", error)
            }
        }
    }
}
```

[https://stackoverflow.com/a/34746109](https://stackoverflow.com/a/34746109)

## App and build version

```swift
// app version
if let appVersion = Bundle.main.infoDictionary?["CFBundleShortVersionString"] as? String {
      // present appVersion
}

if let buildVersion = Bundle.main.infoDictionary?["CFBundleVersion"] as? String {
      // present buildVersion
 }

```

[https://stackoverflow.com/a/59350389](https://stackoverflow.com/a/59350389)

## Providing Access to Directories

[Providing Access to Directories](https://developer.apple.com/documentation/uikit/view_controllers/providing_access_to_directories)

## swiftlint script

```sh
if which swiftlint >/dev/null; then
  swiftlint autocorrect
  swiftlint
else
  echo "warning: SwiftLint not installed, download from https://github.com/realm/SwiftLint"
fi
```

[https://stackoverflow.com/a/57051011](https://stackoverflow.com/a/57051011)

## Using KVO to listen to volume changes

```swift
class YourViewController: UIViewController {

    var obs: NSKeyValueObservation?

    override func viewDidLoad() {
        super.viewDidLoad()

        let audioSession = AVAudioSession.sharedInstance()
        self.obs = audioSession.observe( \.outputVolume ) { (av, change) in
            print("volume \(av.outputVolume)")
        }
    }
}
```

[https://stackoverflow.com/a/51437265](https://stackoverflow.com/a/51437265)
[https://www.ralfebert.de/ios-examples/swift/property-key-value-observer/](https://www.ralfebert.de/ios-examples/swift/property-key-value-observer/)

## Find list of Local Notification the app has already set

```swift
let center = UNUserNotificationCenter.current()

override func viewWillAppear(_ animated: Bool) {
    super.viewWillAppear(animated)

    center.getPendingNotificationRequests { (notifications) in
        print("Count: \(notifications.count)")
        for item in notifications {
          print(item.content)
        }
    }
}

```

[https://stackoverflow.com/a/39034576](https://stackoverflow.com/a/39034576)

## Check if remote push notifications are enabled

```swift
let current = UNUserNotificationCenter.current()

current.getNotificationSettings(completionHandler: { (settings) in
    if settings.authorizationStatus == .notDetermined {
        // Notification permission has not been asked yet, go for it!
    } else if settings.authorizationStatus == .denied {
        // Notification permission was previously denied, go to settings & privacy to re-enable
    } else if settings.authorizationStatus == .authorized {
        // Notification permission was already granted
    }
})
```

[https://stackoverflow.com/a/44407514](https://stackoverflow.com/a/44407514)

## Change the color of a link in an NSMutableAttributedString

> The link color is the tint color of the label/textView. So, you can change it by changing the tint color of the view. However, this will not work if you want different link colours within the same view.

[https://stackoverflow.com/a/33431102](https://stackoverflow.com/a/33431102)

## Present ViewController in full screen

```swift
let detailVC = DetailViewController()
detailVC.modalPresentationStyle = .fullScreen
present(detailVC, animated: true)
```

## objective-c code call swift extension

```swift
extension UIColor {

    // As of Swift 4.0.3, the @objc annotation is needed if you want to use the extension in Objective-C files
    @objc
    class func otherEventColor() -> UIColor {
        return UIColor(red:0.525, green:0.49, blue:0.929, alpha:1)
    }
}
```

Then `#import "ProductModuleName-Swift.h"1 in your ObjC file.

[https://stackoverflow.com/a/32275959](https://stackoverflow.com/a/32275959)

## Delete all Core Data records of an entity

```swift
func deleteAllRecords() {
    let delegate = UIApplication.shared.delegate as! AppDelegate
    let context = delegate.persistentContainer.viewContext

    let deleteFetch = NSFetchRequest<NSFetchRequestResult>(entityName: "CurrentCourse")
    let deleteRequest = NSBatchDeleteRequest(fetchRequest: deleteFetch)

    do {
        try context.execute(deleteRequest)
        try context.save()
    } catch {
        print ("There was an error")
    }
}
```

[https://stackoverflow.com/a/43129221](https://stackoverflow.com/a/43129221)

## Notification send an object

```swift
func post() {
    NotificationCenter.default.post(name: Notification.Name("SomeNotificationName"),
        object: nil, 
        userInfo:["key0": "value", "key1": 1234])
}

func addObservers() {
    NotificationCenter.default.addObserver(self, 
        selector: #selector(someMethod), 
        name: Notification.Name("SomeNotificationName"), 
        object: nil)
}

@objc func someMethod(_ notification: Notification) {
    let info0 = notification.userInfo?["key0"]
    let info1 = notification.userInfo?["key1"]
}
```

[https://stackoverflow.com/a/41366080](https://stackoverflow.com/a/41366080)

## thread-safe access

```swift
let queue = DispatchQueue(label: "thread-safe-obj", attributes: .concurrent)

// write
queue.async(flags: .barrier) {
    // perform writes on data
}

// read
var value: ValueType!
queue.sync {
    // perform read and assign value
}
return value
```

[https://stackoverflow.com/a/28976644](https://stackoverflow.com/a/28976644)

## Use `UIActivityIndicatorView`

```swift
class SpinnerViewController: UIViewController {
    var spinner = UIActivityIndicatorView(style: .whiteLarge)

    override func loadView() {
        view = UIView()
        view.backgroundColor = UIColor(white: 0, alpha: 0.7)

        spinner.translatesAutoresizingMaskIntoConstraints = false
        spinner.startAnimating()
        view.addSubview(spinner)

        spinner.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
        spinner.centerYAnchor.constraint(equalTo: view.centerYAnchor).isActive = true
    }
}

func createSpinnerView() {
    let child = SpinnerViewController()

    // add the spinner view controller
    addChild(child)
    child.view.frame = view.frame
    view.addSubview(child.view)
    child.didMove(toParent: self)

    // wait two seconds to simulate some work happening
    DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
        // then remove the spinner view controller
        child.willMove(toParent: nil)
        child.view.removeFromSuperview()
        child.removeFromParent()
    }
}
```

[https://www.hackingwithswift.com/example-code/uikit/how-to-use-uiactivityindicatorview-to-show-a-spinner-when-work-is-happening](https://www.hackingwithswift.com/example-code/uikit/how-to-use-uiactivityindicatorview-to-show-a-spinner-when-work-is-happening)

## Swift queue

```swift
class Queue<T> {
  private var elements: [T] = []

  func enqueue(_ value: T) {
    elements.append(value)
  }

  func dequeue() -> T? {
    guard !elements.isEmpty else {
      return nil
    }
    return elements.removeFirst()
  }

  var head: T? {
    return elements.first
  }

  var tail: T? {
    return elements.last
  }
}

```

[https://benoitpasquier.com/data-structure-implement-queue-swift/](https://benoitpasquier.com/data-structure-implement-queue-swift/)

## `URLQueryItem`

```swift
import Foundation
import XCPlayground

let queryItems = [URLQueryItem(name: "id", value: "1"), URLQueryItem(name: "id", value: "2")]
var urlComps = URLComponents(string: "www.apple.com/help")!
urlComps.queryItems = queryItems
let result = urlComps.url!
print(result)
```

## `Operation` and `Operation Queue`

[https://www.raywenderlich.com/5293-operation-and-operationqueue-tutorial-in-swift](https://www.raywenderlich.com/5293-operation-and-operationqueue-tutorial-in-swift)

## Send email, sms and phone call

```swift
    func sendEmail(email: String) {
        if MFMailComposeViewController.canSendMail() {
            let mail = MFMailComposeViewController()
            mail.mailComposeDelegate = self
            mail.setToRecipients([email])

            present(mail, animated: true)
        } else {

        }
    }

//MFMailComposeViewControllerDelegate
    func mailComposeController(_ controller: MFMailComposeViewController, didFinishWith result: MFMailComposeResult, error: Error?) {
        controller.dismiss(animated: true)
    }

    func sendSMS(with phoneNumber: String) {
        if MFMessageComposeViewController.canSendText() {
            let messageComposeViewController = MFMessageComposeViewController()
            messageComposeViewController.messageComposeDelegate = self
            messageComposeViewController.recipients = [phoneNumber]
            self.present(messageComposeViewController, animated: true, completion: nil)
        }
    }

// MFMessageComposeViewControllerDelegate
     func messageComposeViewController(_ controller: MFMessageComposeViewController, didFinishWith result: MessageComposeResult) {
        controller.dismiss(animated: true)
    }

    func callNumber(phoneNumber: String) {
        if let url = URL(string: "tel://\(phoneNumber)"), UIApplication.shared.canOpenURL(url) {
            if #available(iOS 10, *) {
                UIApplication.shared.open(url)
            } else {
                UIApplication.shared.openURL(url)
            }
        }
    }
```

## Set the maximum character length of a UITextField

```swift
func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
    let maxLength = 1
    let currentString: NSString = (textField.text ?? "") as NSString
    let newString: NSString =
        currentString.replacingCharacters(in: range, with: string) as NSString
    return newString.length <= maxLength
}
```

[https://stackoverflow.com/a/31363255](https://stackoverflow.com/a/31363255)

## Present view controller push animation

```swift
extension UIViewController {

    func presentDetail(_ viewControllerToPresent: UIViewController) {
        let transition = CATransition()
        transition.duration = 0.25
        transition.type = CATransitionType.push
        transition.subtype = CATransitionSubtype.fromRight
        self.view.window?.layer.add(transition, forKey: kCATransition)

        present(viewControllerToPresent, animated: false)
    }

    func dismissDetail() {
        let transition = CATransition()
        transition.duration = 0.25
        transition.type = CATransitionType.push
        transition.subtype = CATransitionSubtype.fromLeft
        self.view.window?.layer.add(transition, forKey: kCATransition)

        dismiss(animated: false)
    }
}
```

[https://stackoverflow.com/a/42627260](https://stackoverflow.com/a/42627260)

## floating button

```swift
import UIKit

extension UIViewController {
    private struct AssociatedKeys {
        static var floatingButton: UIButton?
    }

    var floatingButton: UIButton? {
        get {
            guard let value = objc_getAssociatedObject(self, &AssociatedKeys.floatingButton) as? UIButton else {return nil}
            return value
        }
        set(newValue) {
            objc_setAssociatedObject(self, &AssociatedKeys.floatingButton, newValue, .OBJC_ASSOCIATION_RETAIN_NONATOMIC)
        }
    }

    func addFloatingButton() {
        // Customize your own floating button UI
        let button = UIButton(type: .custom)
        let image = UIImage(named: "tab_livesupport_unselected")?.withRenderingMode(.alwaysTemplate)
        button.tintColor = .white
        button.setImage(image, for: .normal)
        button.backgroundColor = UIColor.obiletGreen
        button.layer.shadowColor = UIColor.black.cgColor
        button.layer.shadowRadius = 3
        button.layer.shadowOpacity = 0.12
        button.layer.shadowOffset = CGSize(width: 0, height: 1)
        button.sizeToFit()
        let buttonSize = CGSize(width: 60, height: 60)
        let rect = UIScreen.main.bounds.insetBy(dx: 4 + buttonSize.width / 2, dy: 4 + buttonSize.height / 2)
        button.frame = CGRect(origin: CGPoint(x: rect.maxX - 15, y: rect.maxY - 50), size: CGSize(width: 60, height: 60))
        // button.cornerRadius = 30 -> Will destroy your shadows, however you can still find workarounds for rounded shadow.
        button.autoresizingMask = []
        view.addSubview(button)
        floatingButton = button
        let panner = UIPanGestureRecognizer(target: self, action: #selector(panDidFire(panner:)))
        floatingButton?.addGestureRecognizer(panner)
        snapButtonToSocket()
    }

    @objc fileprivate func panDidFire(panner: UIPanGestureRecognizer) {
        guard let floatingButton = floatingButton else {return}
        let offset = panner.translation(in: view)
        panner.setTranslation(CGPoint.zero, in: view)
        var center = floatingButton.center
        center.x += offset.x
        center.y += offset.y
        floatingButton.center = center

        if panner.state == .ended || panner.state == .cancelled {
            UIView.animate(withDuration: 0.3) {
                self.snapButtonToSocket()
            }
        }
    }

    fileprivate func snapButtonToSocket() {
        guard let floatingButton = floatingButton else {return}
        var bestSocket = CGPoint.zero
        var distanceToBestSocket = CGFloat.infinity
        let center = floatingButton.center
        for socket in sockets {
            let distance = hypot(center.x - socket.x, center.y - socket.y)
            if distance < distanceToBestSocket {
                distanceToBestSocket = distance
                bestSocket = socket
            }
        }
        floatingButton.center = bestSocket
    }

    fileprivate var sockets: [CGPoint] {
        let buttonSize = floatingButton?.bounds.size ?? CGSize(width: 0, height: 0)
        let rect = view.bounds.insetBy(dx: 4 + buttonSize.width / 2, dy: 4 + buttonSize.height / 2)
        let sockets: [CGPoint] = [
            CGPoint(x: rect.minX + 15, y: rect.minY + 30),
            CGPoint(x: rect.minX + 15, y: rect.maxY - 50),
            CGPoint(x: rect.maxX - 15, y: rect.minY + 30),
            CGPoint(x: rect.maxX - 15, y: rect.maxY - 50)
        ]
        return sockets
    }
    // Custom socket position to hold Y position and snap to horizontal edges.
    // You can snap to any coordinate on screen by setting custom socket positions.
    fileprivate var horizontalSockets: [CGPoint] {
        guard let floatingButton = floatingButton else {return []}
        let buttonSize = floatingButton.bounds.size
        let rect = view.bounds.insetBy(dx: 4 + buttonSize.width / 2, dy: 4 + buttonSize.height / 2)
        let y = min(rect.maxY - 50, max(rect.minY + 30, floatingButton.frame.minY + buttonSize.height / 2))
        let sockets: [CGPoint] = [
            CGPoint(x: rect.minX + 15, y: y),
            CGPoint(x: rect.maxX - 15, y: y)
        ]
        return sockets
    }
}


override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        addFloatingButton()
        floatingButton?.addTarget(self, action: #selector(floatingButtonPressed), for: .touchUpInside)
    }

    @objc func floatingButtonPressed(){
        print("Floating button tapped")
    }


extension UIApplication{

    class func topViewController(controller: UIViewController? = UIApplication.shared.keyWindow?.rootViewController) -> UIViewController? {
        if let navigationController = controller as? UINavigationController {
            return topViewController(controller: navigationController.visibleViewController)
        }
        if let tabController = controller as? UITabBarController {
            if let selected = tabController.selectedViewController {
                return topViewController(controller: selected)
            }
        }
        if let presented = controller?.presentedViewController {
            return topViewController(controller: presented)
        }
        return controller
    }
}

```

[https://stackoverflow.com/a/55159701](https://stackoverflow.com/a/55159701)

## Cannot use mutating member on immutable value of type

```swift
func someFunc() {
    if var data = data as? ModelOne {
        data.setSub(ModelOne.SubModelOne(someVar: 2, otherVar: 1))
        self.data = data // you can do this since ModelOne conforms to SuperModel
    }
}
```

[https://stackoverflow.com/a/38766080](https://stackoverflow.com/a/38766080)

## Check if the current thread is the main thread

```swift
Thread.isMainThread
```

```objective c
[NSThread isMainThread]
```

## sort an array of objects by two keys

```swift
let sorted = array.sorted { t1, t2 in 
   if t1.isPriority == t2.isPriority {
      return t1.ordering < t2.ordering 
   }
   return t1.isPriority && !t2.isPriority 
}
```

[https://stackoverflow.com/a/29531359](https://stackoverflow.com/a/29531359)