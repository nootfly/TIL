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

