# Sealed classes

* Sealed Classes allow us to fix type hierarchies and forbid developers from creating new subclasses.

* The compiler guarantees that only classes defined in the same source file as the sealed class are able to inherit from it.

* Sealed classes are also implicitly abstract. They should be treated as such throughout the rest of your code, except that nothing else is able to implement them.

* Sealed classes can have fields and methods defined in them, including both abstract and implemented functions. This means that you can have a base representation of the class and then adjust it to suit on the subclasses.

```kotlin
sealed class Expr
data class Const(val number: Double) : Expr()
data class Sum(val e1: Expr, val e2: Expr) : Expr()
object NotANumber : Expr()

fun eval(expr: Expr): Double = when(expr) {
    is Const -> expr.number
    is Sum -> eval(expr.e1) + eval(expr.e2)
    NotANumber -> Double.NaN
    // the `else` clause is not required because we've covered all the cases
}
```

## References

[Sealed Classes](https://kotlinlang.org/docs/reference/sealed-classes.html)

[Sealed Classes in Kotlin](https://www.baeldung.com/kotlin-sealed-classes)