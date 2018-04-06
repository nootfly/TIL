# iOS Extensions access CoreData, shared folder and CloudKit

1. `applicationDocumentsDirectory` needs to point to a group directory.

    ```swift
    public lazy var applicationDocumentsDirectory: URL? = {
       return FileManager.default.containerURL(forSecurityApplicationGroupIdentifier: "group.com.xxx.xxxxxx");
   }()
   ```

2. `sqlite` file is required to put in a group folder

    ```swift
    let coordinator = NSPersistentStoreCoordinator(managedObjectModel: self.managedObjectModel)
       let url = self.applicationDocumentsDirectory?.appendingPathComponent("xxxxx.sqlite")
    ```

3. `CKContainer` is created with a identifier and extensions must share this identifier in targets capabilities settings.

    ```swift
    container = CKContainer(identifier: "iCloud.com.xxx.xxxxxx")
    ```
