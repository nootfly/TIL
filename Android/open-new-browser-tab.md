# Open a link in new Window

```kotlin
fun openNewTabWindow(urls: String, context : Context) {
    val uris = Uri.parse(urls)
    val intents = Intent(Intent.ACTION_VIEW, uris)
    val b = Bundle()
    b.putBoolean("new_window", true)
    intents.putExtras(b)
    context.startActivity(intents)
}
```

[https://stackoverflow.com/a/45959036](https://stackoverflow.com/a/45959036)