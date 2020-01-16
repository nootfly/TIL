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
