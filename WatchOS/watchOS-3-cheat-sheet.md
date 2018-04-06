# watchOS 3 cheat sheet

* The delivery of extension delegate life cycle events may be intermixed with the delivery of activation and deactivation events to the app’s interface controllers, and the order of delivery is not guaranteed. In other words, the `willActivate` method of an interface controller may be called before or after the `applicationDidBecomeActive` method of the extension delegate.

* Use your interface controller’s `init` and `awakeWithContext:` methods to load any required data, set the values for any interface objects, and prepare your interface to be displayed. Do not use the `willActivate` to initialize your interface controller, instead use the `willActivate` method to make last-minute updates before your interface appears onscreen.

* When the user reboots the paired iPhone, Watch apps are still able to run, but they cannot communicate with the iPhone until after the user unlocks it.

* Receiving a background task object from the system is your signal to perform specific types of operations. The task object defines the type of task to perform and contains any data needed to complete the task. The system delivers background task objects to your app by calling the handleBackgroundTasks: method of your app’s extension delegate.

* Background snapshot tasks are budgeted. In general, the system performs approximately one task per hour for each app in the dock (including the most recently used app).  This budget is shared among all complications on the watch face.

* iOS automatically forwards a read-only copy of your iOS app’s preferences to Apple Watch. Your WatchKit extension can read those preferences using an NSUserDefaults object, but it cannot make changes directly to the defaults database.

* Apps can initiate telephone calls or SMS messages using the openSystemURL: method of the shared WKExtension object.
