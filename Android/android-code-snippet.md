# Android code snippets

## Android switch - change background

[https://stackoverflow.com/a/28981942](https://stackoverflow.com/a/28981942)

## get application language and device language

```kotlin
val currentSysLocale = Resources.getSystem().getConfiguration().locales[0]
val currentAppLocale = Locale.getDefault().getLanguage()
Log.d("sys locale","$currentSysLocale")
Log.d("app locale","$currentAppLocale")
```

[https://stackoverflow.com/a/58611147](https://stackoverflow.com/a/58611147)

## Reuse layout

```xml
<layout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto">

    <data>
        <variable name="myText" type="java.lang.String"/>
        <variable name="mySrc" type="android.graphics.drawable.Drawable"/>
    </data>

    <LinearLayout>
        <TextView android:text="@{myText}"/>
        <ImageView android:src="@{mySrc}"/>
    </LinearLayout>
</layout>

<layout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto">

    <LinearLayout>
        <include layout="xxLayout"
            app:myText="@{`aaa`}"
            app:mySrc="@{@drawable/bbb}"/>
        <include layout="xxLayout"
            app:myText="@{`ccc`}"
            app:mySrc="@{@drawable/ddd}"/>
    </LinearLayout>
</layout>
```

[https://stackoverflow.com/a/52881294](https://stackoverflow.com/a/52881294)
