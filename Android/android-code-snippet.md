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
