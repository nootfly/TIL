# Swift UI Code examples

*  How to render a gradient

   ```
    Text("Hello World")
    .padding()
    .foregroundColor(.white)
    .background(LinearGradient(gradient: Gradient(colors: [.white, .red, .black]), startPoint: .top, endPoint: .bottom), cornerRadius: 0)
   ```

* use San Francisco Symbol

  ```
  Image(systemName: "cloud.heavyrain.fill")
    .foregroundColor(.red) 
    .font(.largeTitle)
  ```

* Adjust image

  ```
  Image("example-image")
    .resizable()
    .aspectRatio(contentMode: .fill)
  ```

* Display solid shapes

  ```
  Rectangle()
    .fill(Color.red)
    .frame(width: 200, height: 200)

  Circle()
    .fill(Color.blue)
    .frame(width: 50, height: 50)
  ```

* use images as backgrounds

  ```
   Text("Hacking with Swift")
    .font(.largeTitle)
    .background(
        Image("example-image")
            .resizable()
            .frame(width: 100, height: 100))
  ```

* overlapp content

  ```
   ZStack() {
    Image("example-image")
    Text("Hacking with Swift")
        .font(.largeTitle)
        .background(Color.black)
        .foregroundColor(.white)
    }
  ```

* Random show view

  ```
    var body: some View {
    Group {
        if Bool.random() {
            Image("example-image")
        } else {
            Text("Better luck next time")
        }
    }
   }
  ```

* place content outside the safe area 

  ```
    Text("Hello World")
    .frame(minWidth: 0, maxWidth: .infinity, minHeight: 0, maxHeight: .infinity)
    .background(Color.red)
    .edgesIgnoringSafeArea(.all)
  ```


## References

[https://www.hackingwithswift.com/quick-start/swiftui/how-to-display-solid-shapes](https://www.hackingwithswift.com/quick-start/swiftui/how-to-display-solid-shapes)