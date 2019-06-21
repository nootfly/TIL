# SwiftUI tips and ticks

* Resume the live preview

   `Option-Cmd-P`

* Make `@State` private

  - `@ObjectBinding`  shared between views
  - `@EnvironmentObject` shared by many views
  - `@State` used by the local view

* Prototype with constant bindings

  ```
  TextField(.constant("Hello")).textFieldStyle(.roundedBorder)
  Slider(value: .constant(0.5))

  ```

 * Combine text views

   ```
   struct ContentView : View {
    var body: some View {
        Text("Colored ")
            .color(.red)
        +
        Text("SwifUI ")
                .color(.green)
        +
        Text("Text")
            .color(.blue)
    }
   }
   ``` 

* How to make print() work

   right-click on the play button in the preview canvas and choose `Debug Preview`. With that small change made you’ll find your `print()` calls work as normal.

* Create custom modifiers

  ```
  struct PrimaryLabel: ViewModifier {
    func body(content: Content) -> some View {
        content
            .padding()
            .background(Color.black)
            .foregroundColor(Color.white)
            .font(.largeTitle)
            .cornerRadius(10)
    }
   }
    struct ContentView : View {
    var body: some View {
        Text("Hello World")
            .modifier(PrimaryLabel())
    }
   }
  ```     


## References

[SwiftUI tips and tricks](https://www.hackingwithswift.com/quick-start/swiftui/swiftui-tips-and-tricks)