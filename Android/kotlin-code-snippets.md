# Kotlin Android code sippets

## TextView set typeface

```kotlin
textView.setTypeface(textView.typeface, Typeface.NORMAL)
```

## TextView clickable

```kotlin
fun TextView.setLinkSupport(
    linkText: String,
    callback: () -> Unit
) {
    val spannable = SpannableString(text)
    val pattern: Pattern = Pattern.compile(linkText)
    val matcher = pattern.matcher(spannable)
    while (matcher.find()) {
        val url = spannable.toString().substring(matcher.start(), matcher.end())
        val urlSpan = object : URLSpan(text.toString()) {
            override fun onClick(widget: View) {
                callback()
            }
        }
        spannable.setSpan(urlSpan, matcher.start(), matcher.end(), Spanned.SPAN_EXCLUSIVE_EXCLUSIVE)
        break
    }
    text = spannable
    movementMethod = LinkMovementMethod.getInstance() // Make link clickable
}
```

[https://stackoverflow.com/a/58505945](https://stackoverflow.com/a/58505945)

## `last` and `first` crashes

```kotlin
 val email: EmailsListItem?
        get() = emailsList?.firstOrNull() { it -> it.email.isNotEmpty() }
```

## Test your URLs

[Test your URLs](https://firebase.google.com/docs/app-indexing/android/test)

[Create Deep Links to App Content](https://developer.android.com/training/app-links/deep-linking)

## RecycleView adapter selected index

```kotlin
private var selectedIndex = RecyclerView.NO_POSITION
```

## Returning a result to the previous Destination

need **Navigation 2.3.0-alpha02 and higher**

```kotlin
navController.previousBackStackEntry?.savedStateHandle?.set("key", result)
navController.popBackStack()

override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
    val navController = findNavController();
    // We use a String here, but any type that can be put in a Bundle is supported
    navController.currentBackStackEntry?.savedStateHandle?.getLiveData<String>("key")?.observe(
        viewLifecycleOwner) { result ->
        // Do something with the result.
    }
}
```

[https://stackoverflow.com/a/61239011](https://stackoverflow.com/a/61239011)
[https://developer.android.com/guide/navigation/navigation-programmatic](https://developer.android.com/guide/navigation/navigation-programmatic)
