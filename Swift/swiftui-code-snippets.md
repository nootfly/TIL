# SwiftUI code snippets

## Alert sheet

```swift

@State private var showAlert = false

Text(model.brain.output)
                .font(.system(size: 76))
                .frame(
                    minWidth: 0,
                    maxWidth: .infinity,
                    alignment: .trailing)
                .alert(isPresented: self.$showAlert) {
                    Alert(title: Text("title"), message: Text("message"), primaryButton: .destructive(Text("Copy")){
                        let pasteboard = UIPasteboard.general
                        pasteboard.string = self.model.brain.output
                        }, secondaryButton: .cancel())
                }
                .onTapGesture {
                    self.showAlert = true
            }
```

## Shape backgound and gradient color

```swift
.background(
            RoundedRectangle(cornerRadius: 20)
                .fill(
                    LinearGradient(
                        gradient: Gradient(colors: [.white, .blue]), startPoint: .leading,
                    endPoint: .trailing
                    )
            )
        )
```

## Text rounded rectangular background

```swift
                Text(joke.body)
                    .listRowBackground(RoundedRectangle(cornerRadius: 6)
                        .fill(Color.blue)
```

## detect bottom of list

```swift

struct ContentView: View {

    var body: some View {

        ScrollView {
            ForEach(1...100) { item in
                Text("\(item)")
            }
            Rectangle()
                .onAppear { print("Reached end of scroll view")  }
        }
    }
}

 struct ContentView: View {

    var body: some View {

        List {
            ForEach(1...100) { item in
                Text("\(item)")
            }
            Rectangle()
                .onAppear { print("Reached end of scroll view")  }
        }
    }
  }

```

[https://stackoverflow.com/a/56602782](https://stackoverflow.com/a/56602782)

## WatchOS carousel style

```swift
   List {
       ForEach(items, id:\.self) { item in 
           Text(item)
       }

   }
   .listStyle(CarouselListStyle())
```
