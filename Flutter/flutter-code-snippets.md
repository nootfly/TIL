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

