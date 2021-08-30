# Flutter code snippets (2.2+)

## Place widget in bottom center of the container

```dart
Expanded(
  child: Align(
    alignment: FractionalOffset.bottomCenter,
      child: Padding(
        padding: EdgeInsets.only(bottom: 10.0),
          child: //Your widget here,
    ),
  ),
),
```

[https://stackoverflow.com/a/58213329](https://stackoverflow.com/a/58213329)

## Print log messages

```dart
debugPrintStack();
```

## Enum from string

```dart
enum Fruit { apple, banana }

// Convert to string
String str = Fruit.banana.toString();

// Convert to enum
Fruit f = Fruit.values.firstWhere((e) => e.toString() == str);

assert(f == Fruit.banana);  // it worked
```

[https://stackoverflow.com/a/44060511](https://stackoverflow.com/a/44060511)


## Disable text field

```dart
TextField(
  readOnly: true,
  enableInteractiveSelection: false,
  onTap: () {
    do_something(),
  },
)
```
[https://flutteragency.com/disable-textfield-in-flutter/](https://flutteragency.com/disable-textfield-in-flutter/)


## display markdown

```dart
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_markdown/flutter_markdown.dart';

class PrivacyPolicyScreen extends StatelessWidget {
  const PrivacyPolicyScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SafeArea(
        child: Scaffold(
      appBar: AppBar(
        title: const Text('Privacy Terms & Policy'),
      ),
      body: FutureBuilder(
          future: rootBundle.loadString("assets/privacy_terms.md"),
          builder: (BuildContext context, AsyncSnapshot<String> snapshot) {
            if (snapshot.hasData) {
              return Markdown(data: snapshot.data ?? '');
            }

            return const Center(
              child: CircularProgressIndicator(),
            );
          }),
    ));
  }
}
```

[https://developer.school/how-to-display-markdown-in-flutter/](https://developer.school/how-to-display-markdown-in-flutter/)