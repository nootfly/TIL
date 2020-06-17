# executePendingBindings

> Evaluates the pending bindings, updating any Views that have expressions bound to modified variables. This must be run on the UI thread.

> Calling executePendingBindings means that you're essentially forcing the framework to do everything it needs to do so far on the binding, right at the moment of calling it.

[https://stackoverflow.com/a/53043911](https://stackoverflow.com/a/53043911)