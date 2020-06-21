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

## Push View programmatically in callback

```swift

NavigationLink(destination: ProfileView(viewModel: ProfileViewModelImpl()), isActive: self.pushActive) {
    Text("")
  }.hidden()
```

[https://stackoverflow.com/a/57321795](https://stackoverflow.com/a/57321795)

## How to render a gradient

```swift
    Text("Hello World")
    .padding()
    .foregroundColor(.white)
    .background(LinearGradient(gradient: Gradient(colors: [.white, .red, .black]), startPoint: .top, endPoint: .bottom), cornerRadius: 0)
```

## use San Francisco Symbol

```swift
  Image(systemName: "cloud.heavyrain.fill")
    .foregroundColor(.red) 
    .font(.largeTitle)
```

## Adjust image

```swift
  Image("example-image")
    .resizable()
    .aspectRatio(contentMode: .fill)
```

## Display solid shapes

```swift
  Rectangle()
    .fill(Color.red)
    .frame(width: 200, height: 200)

  Circle()
    .fill(Color.blue)
    .frame(width: 50, height: 50)
```

## use images as backgrounds

```swift
   Text("Hacking with Swift")
    .font(.largeTitle)
    .background(
        Image("example-image")
            .resizable()
            .frame(width: 100, height: 100))
```

## overlapp content

```swift
   ZStack() {
    Image("example-image")
    Text("Hacking with Swift")
        .font(.largeTitle)
        .background(Color.black)
        .foregroundColor(.white)
    }
```

## Random show view

```swift
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

## place content outside the safe area

```swift
    Text("Hello World")
    .frame(minWidth: 0, maxWidth: .infinity, minHeight: 0, maxHeight: .infinity)
    .background(Color.red)
    .edgesIgnoringSafeArea(.all)
```

[https://www.hackingwithswift.com/quick-start/swiftui/how-to-display-solid-shapes](https://www.hackingwithswift.com/quick-start/swiftui/how-to-display-solid-shapes)

## WatchOS environment object

```swift
class HostingController: WKHostingController<AnyView> {
    override var body: AnyView {
        return  AnyView(ContentView().environmentObject(Store()))
    }
}
```

[https://stackoverflow.com/a/56555883](https://stackoverflow.com/a/56555883)

## WatchOS context menu

```swift
var body: some View {
    Group {
        Text("Hello Daymo")
    }
    .contextMenu(menuItems: {
        Button(action: {
            print("Refresh")
        }, label: {
            VStack{
                Image(systemName: "arrow.clockwise")
                    .font(.title)
                Text("Refresh view")
            }
        })
    })
}
```

[https://stackoverflow.com/a/57677049](https://stackoverflow.com/a/57677049)

## WatchOS load pages dynamically

```swift
class HostingController: WKHostingController<MainView> {
    override var body: MainView {
        return MainView(host: self)
    }

    func reloadPages() {
        var namesAndContexts:[(name: String, context: AnyObject)]
        if UserDefaults.standard.bool(forKey: "key") {
            namesAndContexts =
        } else {
             namesAndContexts =
        }
         WKInterfaceController.reloadRootControllers(withNamesAndContexts: namesAndContexts)
    }


}

struct MainView : View {
    weak var host: HostingController?
    var body: some View {
        Text("")
            .onAppear(perform: {
                self.host?.reloadPages()
            })

    }
}
```

## Search bar

```swift

import SwiftUI

struct ContentView: View {
    let array = ["Peter", "Paul", "Mary", "Anna-Lena", "George", "John", "Greg", "Thomas", "Robert", "Bernie", "Mike", "Benno", "Hugo", "Miles", "Michael", "Mikel", "Tim", "Tom", "Lottie", "Lorrie", "Barbara"]
    @State private var searchText = ""
    @State private var showCancelButton: Bool = false

    var body: some View {

        NavigationView {
            VStack {
                // Search view
                HStack {
                    HStack {
                        Image(systemName: "magnifyingglass")

                        TextField("search", text: $searchText, onEditingChanged: { isEditing in
                            self.showCancelButton = true
                        }, onCommit: {
                            print("onCommit")
                        }).foregroundColor(.primary)

                        Button(action: {
                            self.searchText = ""
                        }) {
                            Image(systemName: "xmark.circle.fill").opacity(searchText == "" ? 0 : 1)
                        }
                    }
                    .padding(EdgeInsets(top: 8, leading: 6, bottom: 8, trailing: 6))
                    .foregroundColor(.secondary)
                    .background(Color(.secondarySystemBackground))
                    .cornerRadius(10.0)

                    if showCancelButton  {
                        Button("Cancel") {
                                UIApplication.shared.endEditing(true) // this must be placed before the other commands here
                                self.searchText = ""
                                self.showCancelButton = false
                        }
                        .foregroundColor(Color(.systemBlue))
                    }
                }
                .padding(.horizontal)
                .navigationBarHidden(showCancelButton) // .animation(.default) // animation does not work properly

                List {
                    // Filtered list of names
                    ForEach(array.filter{$0.hasPrefix(searchText) || searchText == ""}, id:\.self) {
                        searchText in Text(searchText)
                    }
                }
                .navigationBarTitle(Text("Search"))
                .resignKeyboardOnDragGesture()
            }
        }
    }
}



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

extension UIApplication {
    func endEditing(_ force: Bool) {
        self.windows
            .filter{$0.isKeyWindow}
            .first?
            .endEditing(force)
    }
}

struct ResignKeyboardOnDragGesture: ViewModifier {
    var gesture = DragGesture().onChanged{_ in
        UIApplication.shared.endEditing(true)
    }
    func body(content: Content) -> some View {
        content.gesture(gesture)
    }
}

extension View {
    func resignKeyboardOnDragGesture() -> some View {
        return modifier(ResignKeyboardOnDragGesture())
    }
}

```

[https://stackoverflow.com/a/58473985](https://stackoverflow.com/a/58473985)

## Button image not showing

```swift
                Button(action: {
                }){
                    Image("settings_icon")

                }
                .buttonStyle(PlainButtonStyle())
```

## Button action in a list or a form

```swift
                Button(action: {
                  //keep empty
                }) {
                    HStack {
                        Text("Test")
                    }
                    .onTapGesture {
                        //real action
                    }

                    .buttonStyle(BorderlessButtonStyle())

                }
```

## Dismiss presented window

```swift
@Environment(\.presentationMode) var presentationMode: Binding<PresentationMode>

self.presentationMode.wrappedValue.dismiss()
```

[https://stackoverflow.com/a/56563652](https://stackoverflow.com/a/56563652)

## ObserveredObject does not get updates only in ScrollView. It can get updates in List.

## Content in scrollview as a list item disappears when scrolling

```swift
struct ItemView: View {
    var body: some View {
        VStack {
            Text("Tag list:")
            ScrollView(.horizontal, showsIndicators: false) {
                HStack {
                    ForEach(0...8, id: \.self) { _ in
                        TagView().padding()
                    }
                }
            }.id(UUID().uuidString) // << here is a fix !
        }
    }
}
```

[https://stackoverflow.com/a/59811359](https://stackoverflow.com/a/59811359)

## NavigationView broken in rotation

```swift
NavigationView {
//views
}
.navigationViewStyle(StackNavigationViewStyle())

```

[https://forums.developer.apple.com/thread/119691](https://forums.developer.apple.com/thread/119691)

## `contextMenu`

```swift
Text("Control Click Me")
    .contextMenu {
        Button(action: { print("added") } ) { Text("Add") }
        Button(action: { print("removed") } ) { Text("Remove") }
    }
```

[https://developer.apple.com/documentation/swiftui/view/3288993-contextmenu](https://developer.apple.com/documentation/swiftui/view/3288993-contextmenu)

## Multiple sheets

```swift
enum ActiveSheet {
   case first, second
}

struct ContentView: View {

    @State private var showSheet = false
    @State private var activeSheet: ActiveSheet = .first

    var body: some View {

        NavigationView {
            VStack(spacing: 20) {
                Button("First modal view") {
                    self.showSheet = true
                    self.activeSheet = .first
                }
                Button ("Second modal view") {
                    self.showSheet = true
                    self.activeSheet = .second
                }
            }
            .navigationBarTitle(Text("Multiple modal view problem"), displayMode: .inline)
            .sheet(isPresented: $showSheet) {
                if self.activeSheet == .first {
                    Text("First modal view")
                }
                else {
                    Text("Only the second modal view works!")
                }
            }
        }
    }
}
```

[https://stackoverflow.com/a/58837261](https://stackoverflow.com/a/58837261)

## Update FetchRequest

```swift
@State private var refreshing = false
private var didSave =  NotificationCenter.default.publisher(for: .NSManagedObjectContextDidSave)

var body: some View {
    List {
        ForEach(fetchedResults) { primary in
            NavigationLink(destination: SecondaryView(primary: primary)) {
                VStack(alignment: .leading) {
                    // below use of .refreshing is just as demo,
                    // it can be use for anything
                    Text("\(primary.primaryName ?? "nil")" + (self.refreshing ? "" : ""))
                    Text("\(primary.secondary?.secondaryName ?? "nil")").font(.footnote).foregroundColor(.secondary)
                }
            }
            // here is the listener for published context event
            .onReceive(self.didSave) { _ in
                self.refreshing.toggle()
            }
        }
    }
    .navigationBarTitle("Primary List")
    .navigationBarItems(trailing:
        Button(action: {self.addNewPrimary()} ) {
            Image(systemName: "plus")
        }
    )
}
```

[https://stackoverflow.com/a/58777603](https://stackoverflow.com/a/58777603)


## WatchOS `digitalCrownRotation`

```swift
   Text("\(Int(selection))")
                    .padding()
                    .digitalCrownRotation($selection, from: 1.0, through: 10.0, by: 1.0, sensitivity: .low, isContinuous: false, isHapticFeedbackEnabled: true)
```

[https://developer.apple.com/documentation/swiftui/color/3298184-digitalcrownrotation](https://developer.apple.com/documentation/swiftui/color/3298184-digitalcrownrotation)

## `GeometryReader`

```swift
struct SimpleLineView: View {
    var width: Float
    var body: some View {
        GeometryReader { geometry in
            RoundedRectangle(cornerRadius: 25, style: .continuous)
                .path(in: CGRect(x:0,
                                 y: 0,
                                 width: geometry.size.width * CGFloat(self.width / 10.0),
                                 height: geometry.size.height))
                .fill(Color.orange)

        }
    }
}
```

[https://swiftui-lab.com/geometryreader-to-the-rescue/](https://swiftui-lab.com/geometryreader-to-the-rescue/)

## Hide navigation bar

```swift
    var body: some View {
        VStack {
            Button("Done", action: dismiss)
        }
         .navigationBarHidden(true)
         .edgesIgnoringSafeArea([.top])
    }
```

## Equal widths of subviews with SwiftUI

```swift
var body: some View {
    VStack {
        HStack(spacing: 0) {

            VStack {
                Text("Short").font(.body)
            }
                .frame(minWidth: 0, maxWidth: .infinity)
                .background(Color.green)

            VStack {
                Text("Longer!!!").font(.body)
            }
                .frame(minWidth: 0, maxWidth: .infinity)
                .background(Color.blue)

        }
            .frame(minWidth: 0, maxWidth: .infinity)
            .background(Color.yellow)
        Button (action: doSomething) {
            Text("|")
        }
    }
}
```

[https://stackoverflow.com/a/56620897](https://stackoverflow.com/a/56620897)

## iPad `DoubleColumnNavigationViewStyle`

```swift
var body: some View {

        NavigationView {

            MyMasterView()

            DetailsView()

        }.navigationViewStyle(DoubleColumnNavigationViewStyle())
         .padding()
    }
```

[https://stackoverflow.com/a/57215664](https://stackoverflow.com/a/57215664)

[https://stackoverflow.com/a/57400873](https://stackoverflow.com/a/57400873)
