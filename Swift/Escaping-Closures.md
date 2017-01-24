# Escaping Closures in Swift 3.0.1

A closure is said to escape a function when the closure is passed as an argument to the function, but is called after the function returns. When you declare a function that takes a closure as one of its parameters, you can write `@escaping` before the parameter’s type to indicate that the closure is allowed to escape.

Marking a closure with `@escaping` means you have to refer to self explicitly within the closure. Marking a closure with `@escaping` means you have to refer to self explicitly within the closure. 

The content is from [The Swift Programming Language (Swift 3.0.1)](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/Closures.html)
