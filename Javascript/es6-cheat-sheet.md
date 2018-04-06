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

35. You can initialize a map with data by passing an array to the Map constructor. Each item in the array must itself be an array where the first item is the key and the second is that key’s corresponding value. Therefore, the entire map is an array of these two-item arrays.

36. It’s best to use weak sets only for tracking objects that need to be grouped together.

37. Generator functions are indicated by an asterisk character (*) after the function keyword and use the new yield keyword.

38. The for-of statement will throw an error when you use it on a non-iterable object, null, or undefined.

39. The spread operator and `for-of` ignore any value specified by a return statement. As soon as they see done is true, they stop without reading the value. However, iterator return values are helpful when delegating generators.

40. Class declarations and class expressions are not hoisted.

41. Classes that inherit from other classes are referred to as derived classes. Derived classes require you to use `super()` if you specify a constructor; if you don’t, an error will occur. You must call `super()` before accessing this in the constructor. Because `super()` is responsible for initializing this, attempting to access this before calling `super()` results in an error. The only way to avoid calling `super()` is to return an object from the class constructor.

42. An internal [[PromiseState]] property is set to "pending", "fulfilled", or "rejected" to reflect the promise’s state. This property isn’t exposed on promise objects, so you can’t determine which state the promise is in programmatically. But you can take a specific action when a promise changes state by using the then() method.

43. Prototype proxy traps have some restrictions. First, the getPrototypeOf trap must return an object or null, and any other return value results in a runtime error. The return value check ensures that Object.getPrototypeOf() will always return an expected value. Second, the return value of the setPrototypeOf trap must be false if the operation doesn’t succeed. When setPrototypeOf returns false, Object.setPrototypeOf() throws an error. If setPrototypeOf returns any value other than false, Object.setPrototypeOf() assumes the operation succeeded.

44. You can use the ownKeys trap to, for example, filter out certain property keys that you don’t want used when the Object.keys() method, the Object.getOwnPropertyNames() method, the Object.getOwnPropertySymbols() method, or the Object.assign() method is used.

45. Using a combination of proxy traps and reflection API methods, it’s possible to filter some operations to behave differently only in certain conditions while defaulting to the built-in behavior.

46. A module is JavaScript code that automatically runs in strict mode with no way to opt out. Keep in mind that no matter how many times you use a module in import statements, the module will execute only once. Keep in mind that the default must come before the non-defaults in the import statement. Imports without bindings are most likely to be used to create polyfills and shims.


Reference:

* [ECMAScript 6 Tutorial](http://ccoenraets.github.io/es6-tutorial/)
* Understanding ECMAScript 6
