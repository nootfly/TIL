# Lazy delegate

lazy() is a function that takes a lambda and returns an instance of Lazy<T> which can serve as a delegate for implementing a lazy property: the first call to get() executes the lambda passed to lazy() and remembers the result, subsequent calls to get() simply return the remembered result.

```kotlin
val lazyValue: String by lazy {
    println("computed!")
    "Hello"
}

fun main() {
    println(lazyValue)
    println(lazyValue)
}

computed!
Hello
Hello
```

## References

[Delegated Properties](https://kotlinlang.org/docs/reference/delegated-properties.html)

[https://stackoverflow.com/a/36623703](https://stackoverflow.com/a/36623703)