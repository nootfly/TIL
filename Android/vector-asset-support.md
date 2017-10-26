# Support Library

This technique requires Android Support Library 23.2 or higher and Android Plugin for Gradle 2.0 or higher, and uses vector drawables only. The VectorDrawableCompat class in the Support Library allows you to support VectorDrawable in Android 2.1 (API level 7) and higher.

Before using Vector Asset Studio, you must add a statement to your build.gradle file:

```groovy
android {
  defaultConfig {
    vectorDrawables.useSupportLibrary = true
  }
}

dependencies {
  compile 'com.android.support:appcompat-v7:23.2.0'
}
```

Reference:
[https://developer.android.com/studio/write/vector-asset-studio.html](https://developer.android.com/studio/write/vector-asset-studio.html)