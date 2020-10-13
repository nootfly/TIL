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

## Android Data Binding using include tag

```xml
<layout xmlns:andr...>
  <Button
    android:id="@+id/button"
     />
    <layout xmlns:andr...
   <include layout="@layout/buttons"
            android:id="@+id/buttons"/>
```

```kotlin
MainBinding binding = MainBinding.inflate(getLayoutInflater());
binding.buttons.button
```

[https://stackoverflow.com/a/32958608](https://stackoverflow.com/a/32958608)

## Button text not ALL CAPS

Use this line `android:textAllCaps="false"` in your xml

```xml
<Button
            android:id="@+id/btn_login"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="@string/login_str"
            android:background="@color/colorBlue"
            android:textColor="@color/colorWhite"
            android:textAllCaps="false"
           />
```

[https://stackoverflow.com/a/59212391](https://stackoverflow.com/a/59212391)

## Combine multiple live data

```kotlin

fun blogpostBoilerplateExample(newUser: String): LiveData<UserDataResult> {

val liveData1 = userOnlineDataSource.getOnlineTime(newUser)
val liveData2 = userCheckinsDataSource.getCheckins(newUser)

val result = MediatorLiveData<UserDataResult>()

result.addSource(liveData1) { value ->
    result.value = combineLatestData(liveData1, liveData2)
}
result.addSource(liveData2) { value ->
    result.value = combineLatestData(liveData1, liveData2)
}
return result
}

private fun combineLatestData(
    onlineTimeResult: LiveData<Long>,
    checkinsResult: LiveData<CheckinsResult>
): UserDataResult {

val onlineTime = onlineTimeResult.value
val checkins = checkinsResult.value

// Don't send a success until we have both results
if (onlineTime == null || checkins == null) {
    return UserDataLoading()
}

// TODO: Check for errors and return UserDataError if any.

return UserDataSuccess(timeOnline = onlineTime, checkins = checkins)
}
```

[https://stackoverflow.com/a/56843092](https://stackoverflow.com/a/56843092)

## Display HTML in `TextView`

```kotlin
 val htmlString = "<span style=\\\"font-family: 'Campton-Light','-apple-system', 'HelveticaNeue'; color: '#000000';font-size: \\(16)\\\">${item.text}</span>"
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
               binding.detail.text = Html.fromHtml(htmlString, Html.FROM_HTML_MODE_COMPACT)
            } else {
                binding.detail.text = Html.fromHtml(htmlString)
            }
```

[https://stackoverflow.com/a/2116191](https://stackoverflow.com/a/2116191)

## convert date string to another format

```kotlin
fun convertDateFormatFromDashboardFormat(date: String?): String {
    if (date == null) {
        return ""
    }
    try {
        var dateFormat = DateTimeFormatterBuilder()
            .parseCaseInsensitive()
            .appendPattern("dd MMM yyyy")
            .toFormatter(Locale.ENGLISH)


        val date = dateFormat.parse(date)
        dateFormat = DateTimeFormatterBuilder()
            .parseCaseInsensitive()
            .appendPattern("dd/MM/yyyy")
            .toFormatter(Locale.ENGLISH)
        return dateFormat.format(date)

    } catch (e: DateTimeParseException) {
        Timber.d(e)

    }
    return ""
}
```

[https://stackoverflow.com/a/44707392](https://stackoverflow.com/a/44707392)

## Enable textview html link

Do not set `android:autoLink="all"` or `a`ndroid:autoLink="web"` in the xml, because with that **it doesn't work!**

```kotlin
  if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
            textView.text = Html.fromHtml(htmlString, Html.FROM_HTML_MODE_LEGACY)
        } else {
            textView.text = Html.fromHtml(htmlString)
        }
        textView.isClickable = true
        textView.movementMethod = LinkMovementMethod.getInstance()
```

[https://stackoverflow.com/a/59046991](https://stackoverflow.com/a/59046991)
