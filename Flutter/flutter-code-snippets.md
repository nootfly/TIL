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