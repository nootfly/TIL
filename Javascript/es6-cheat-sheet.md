# ES6 cheat sheet

1.  Unlike variables declared with var that are function-scoped, variables declared with let are block-scoped: they only exist in the block they are defined in.

2. In the Chrome Development Tool > Network > Disable Cache

3. Modules have been available in JavaScript through third-party libraries. ECMAScript 6 adds native support for modules to JavaScript. When you compile a modular ECMAScript 6 application to ECMASCript 5, the compiler relies on a third party library to implement modules in ECMAScript 5. Webpack and Browserify are two popular options, and Babel supports both (and others).

4. The ECMAScript 6 arrow function syntax is a shorthand for the ECMAScript 5 function syntax. It supports both block and expression bodies. The value of this inside the function is not altered: it is the same as the value of this outside the function. No more var self = this to keep track of the current scope.

5. Current browsers don’t support all the new ECMAScript 6 (aka ECMAScript 2015) features yet (see comptability table). You need to use a compiler (transpiler) to transform your ECMAScript 6 code to ECMAScript 5 compatible code. Although there are other options, Babel has become the de-facto standard to compile ECMAScript 6 applications to a version of ECMAScript that can run in current browsers. Babel can also compile other versions of ECMAScript as well as React’s JSX.

6. Promises have replaced callback functions as the preferred programming style for handling asynchronous calls. A promise is a holder for a result (or an error) that will become available in the future (when the async call returns). Promises have been available in JavaScript through third-party libraries (for example, jQuery and q). ECMAScript 6 adds built-in support for promises to JavaScript.

7. What you know as JavaScript in browsers and in Node.js is actually a superset of ECMAScript

8. Bindings declared using const are considered constants, meaning their values cannot be changed once set.

9. Constants, like let declarations, are block-level declarations. That means constants are no longer accessible once execution flows out of the block in which they were declared, and declarations are not hoisted.

10. The value a constant holds can be modified if it is an object. `const` prevents modification of the binding, not modification of the bound value.

11. Use const by default, and only use let when you know a variable’s value needs to change.

12. ECMAScript 6 supports Unicode normalization forms by giving strings a `normalize()` method.

13. ECMAScript 6 adds `includes()`, `startsWith()`, `endsWith()` and `repeat()` method to strings.

14. A template tag performs a transformation on the template literal and returns the final string value. This tag is specified at the start of the template.

15. Rest parameters have two restrictions. The first restriction is that there can be only one rest parameter, and the rest parameter must be last. The second restriction is that rest parameters cannot be used in an object literal setter.

16. All functions in an ECMAScript 6 program will have an appropriate value for their name property.

17. JavaScript has two different internal-only methods for functions: [[Call]] and [[Construct]]. When a function is called without new, the [[Call]] method is executed, which executes the body of the function as it appears in the code. When a function is called with new, that’s when the [[Construct]] method is called.

18. ECMAScript 6 introduces the new.target metaproperty. A metaproperty is a property of a nonobject that provides additional information related to its target (such as new).

19. Block-level functions are hoisted to the top of the block in which they are defined.

20. But arrow functions behave differently than traditional JavaScript functions in a number of important ways: 1. No this, super, arguments, and new.target bindings 2. Cannot be called with new 3. No prototype 4. Can’t change this 5. No arguments object 6. No duplicate named parameters.

21. Even though there is no explicit return statement, this arrow function will return the first argument that is passed in.

22. Think about tail call optimization whenever you’re writing a recursive function, because it can provide a significant performance improvement, especially when applied in a computationally expensive function.

23. When an object property name is the same as the local variable name, you can simply include the name without a colon and value.

24. ECMAScript 6 introduces the `Object.is()` method to remedy the remaining inaccuracies of the identically equals operator.

25. It’s now possible to modify an object’s prototype after it’s been created thanks to ECMAScript 6’s Object.setPrototypeOf() method.

26. When you’re using destructuring to declare variables using var, let, or const, you must supply an initializer (the value after the equal sign).

27. In ECMAScript 6, you can use rest items to clone an array.

28. ECMAScript 6 introduces symbols as a primitive type. (The language already had five primitive types: strings, numbers, Booleans, null, and undefined.

29. ECMAScript 6 introduces symbols as a primitive type. (The language already had five primitive types: strings, numbers, Booleans, null, and undefined.

30. ECMAScript 6 added sets and maps to JavaScript.

31. Keep in mind that although sets are great for tracking values and forEach() lets you work on each item sequentially, you can’t directly access an item by index like you can with an array. If you need to do so, the best option is to convert the set to an array.

32. Converting an array to a set is easy because you can pass the array to the Set constructor; converting a set back to an array is also easy if you use the spread operator (...).

33. ECMAScript 6 also includes weak sets, which only store weak object references and cannot store primitive values. A weak reference to an object doesn’t prevent garbage collection if it’s the only remaining reference.

34. Keep in mind that an error will be thrown if the array contains any nonobject values, because WeakSet can’t accept primitive values.




Reference:

* [ECMAScript 6 Tutorial](http://ccoenraets.github.io/es6-tutorial/)
* Understanding ECMAScript 6
