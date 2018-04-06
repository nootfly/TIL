#CoreData in Swift framework

Three things are required when CoreData is put in a Swift framework and this framework is shared between the main project and extension projects. Reference: https://www.andrewcbancroft.com/2015/08/25/sharing-a-core-data-model-with-a-swift-framework/

- Need to create a data model file in this Swift framework. You cannot move one from other projects.

- Create an app group for sqlite database
```swift
lazy var applicationDocumentsDirectory: NSURL = {  
        let url = NSFileManager.defaultManager().containerURLForSecurityApplicationGroupIdentifier("group.xxx.xxxxxx");
        return url!
    }()
```
- Use the framework bundle to get the data model file
```swift
lazy var managedObjectModel: NSManagedObjectModel = {
       let shareKitBundle = NSBundle(identifier: "com.xxx.xxxxxx")
       let modelURL = shareKitBundle!.URLForResource("DataModel", withExtension: "momd")!
       return NSManagedObjectModel(contentsOfURL: modelURL)!
   }()
```
