# CoreData get records count

  ```swift
  let fetchRequest = NSFetchRequest<NSFetchRequestResult>(entityName: "entityName")
      fetchRequest.includesSubentities = false
     do {
         return try managedObjectContext.count(for: fetchRequest)
     } catch {
         print("fetch error")
     }
     return 0
  ```
