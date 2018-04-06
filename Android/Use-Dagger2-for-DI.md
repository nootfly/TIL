# Use Dagger 2 for dependency injection

This quote is from Google
>Dependency injection frameworks can simplify the code you write and provide an adaptive environment that's useful for testing and other configuration changes.

>If you intend to use a dependency injection framework in your app, consider using Dagger 2. Dagger does not use reflection to scan your app's code. Dagger's static, compile-time implementation means that it can be used in Android apps without needless runtime cost or memory usage.

>Other dependency injection frameworks that use reflection tend to initialize processes by scanning your code for annotations. This process can require significantly more CPU cycles and RAM, and can cause a noticeable lag when the app launches.

Reference:
[https://developer.android.com/topic/performance/memory.html#DependencyInjection](https://developer.android.com/topic/performance/memory.html#DependencyInjection)

