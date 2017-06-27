# ES6 cheat sheet

1.  Unlike variables declared with var that are function-scoped, variables declared with let are block-scoped: they only exist in the block they are defined in.

2. In the Chrome Development Tool > Network > Disable Cache

3. Modules have been available in JavaScript through third-party libraries. ECMAScript 6 adds native support for modules to JavaScript. When you compile a modular ECMAScript 6 application to ECMASCript 5, the compiler relies on a third party library to implement modules in ECMAScript 5. Webpack and Browserify are two popular options, and Babel supports both (and others).

4. The ECMAScript 6 arrow function syntax is a shorthand for the ECMAScript 5 function syntax. It supports both block and expression bodies. The value of this inside the function is not altered: it is the same as the value of this outside the function. No more var self = this to keep track of the current scope.

5. Current browsers don’t support all the new ECMAScript 6 (aka ECMAScript 2015) features yet (see comptability table). You need to use a compiler (transpiler) to transform your ECMAScript 6 code to ECMAScript 5 compatible code. Although there are other options, Babel has become the de-facto standard to compile ECMAScript 6 applications to a version of ECMAScript that can run in current browsers. Babel can also compile other versions of ECMAScript as well as React’s JSX.

6. Promises have replaced callback functions as the preferred programming style for handling asynchronous calls. A promise is a holder for a result (or an error) that will become available in the future (when the async call returns). Promises have been available in JavaScript through third-party libraries (for example, jQuery and q). ECMAScript 6 adds built-in support for promises to JavaScript.

7. What you know as JavaScript in browsers and in Node.js is actually a superset of ECMAScript

8. Bindings declared using const are considered constants, meaning their values cannot be changed once set.


Reference:

* [ECMAScript 6 Tutorial](http://ccoenraets.github.io/es6-tutorial/)
* Understanding ECMAScript 6
