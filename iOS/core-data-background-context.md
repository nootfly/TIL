# core data background context

```swift
let context = persistentContainer.newBackgroundContext()
context.automaticallyMergesChangesFromParent = true

context.perform {
  let howMany = 999
  for index in 1...howMany{
    let person = Person(context: context)
    person.firstName = "First name \(index)"
    person.lastName = "First name \(index)"
  }
  do{
    try context.save()
    DispatchQueue.main.async{completion()}
  } catch {
    // catch the errors here
  }

}
```