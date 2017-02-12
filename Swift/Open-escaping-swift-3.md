# open and @escaping in Swift 3

* [`open` keyword](http://stackoverflow.com/a/38950955/1146834)

* A closure is said to escape a function when the closure is passed as an argument to the function, but is called after the function returns. When you declare a function that takes a closure as one of its parameters, you can write `@escaping` before the parameter’s type to indicate that the closure is allowed to escape. If you didn’t mark the parameter of this function with `@escaping`, you would get a compile-time error. Marking a closure with `@escaping` means you have to refer to self explicitly within the closure.(https://developer.apple.com/library/prerelease/content/documentation/Swift/Conceptual/Swift_Programming_Language/Closures.html)
