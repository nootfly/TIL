# SwiftUI code



## preview your layout in light and dark mode

[https://www.hackingwithswift.com/quick-start/swiftui/how-to-preview-your-layout-in-light-and-dark-mode](https://www.hackingwithswift.com/quick-start/swiftui/how-to-preview-your-layout-in-light-and-dark-mode)

```swift
#if DEBUG
struct ContentView_Previews: PreviewProvider {
   static var previews: some View {
      Group {
         ContentView()
            .environment(\.colorScheme, .light)

         ContentView()
            .environment(\.colorScheme, .dark)
      }
   }
}
#endif
```


## Adjust accent color of a view

[https://www.hackingwithswift.com/quick-start/swiftui/how-to-adjust-the-accent-color-of-a-view](https://www.hackingwithswift.com/quick-start/swiftui/how-to-adjust-the-accent-color-of-a-view)

```swift
VStack {
    Button(action: {}) {
        Text("Tap here")
    }
}.accentColor(.orange)
```