# Automatic Reference Counting

* Swift provides two ways to resolve strong reference cycles when you work with properties of class type: weak references and unowned references.

* Weak and unowned references enable one instance in a reference cycle to refer to the other instance without keeping a strong hold on it. The instances can then refer to each other without creating a strong reference cycle.

* Use a weak reference when the other instance has a shorter lifetime—that is, when the other instance can be deallocated first. In contrast, use an unowned reference when the other instance has the same lifetime or a longer lifetime.

* Because weak references need to allow their value to be changed to nil at runtime, they are always declared as variables, rather than constants, of an optional type.

* Property observers aren’t called when ARC sets a weak reference to nil.

* An unowned reference is expected to always have a value. As a result, ARC never sets an unowned reference’s value to nil, which means that unowned references are defined using nonoptional types.

* Use an unowned reference only when you are sure that the reference always refers to an instance that has not been deallocated. If you try to access the value of an unowned reference after that instance has been deallocated, you’ll get a runtime error.

* A CreditCard instance never outlives the Customer that it refers to. To represent this, the Customer class has an optional card property, but the CreditCard class has an unowned (and nonoptional) customer property.

* Swift also provides unsafe unowned references for cases where you need to disable runtime safety checks—for example, for performance reasons. As with all unsafe operations, you take on the responsibility for checking that code for safety.

* You indicate an unsafe unowned reference by writing unowned(unsafe). If you try to access an unsafe unowned reference after the instance that it refers to is deallocated, your program will try to access the memory location where the instance used to be, which is an unsafe operation.

* However, there is a third scenario, in which both properties should always have a value, and neither property should ever be nil once initialization is complete. In this scenario, it’s useful to combine an unowned property on one class with an implicitly unwrapped optional property on the other class.

* The initializer for City is called from within the initializer for Country. However, the initializer for Country cannot pass self to the City initializer until a new Country instance is fully initialized, as described in Two-Phase Initialization.

```swift
class Country {
    let name: String
    var capitalCity: City!
    init(name: String, capitalName: String) {
        self.name = name
        self.capitalCity = City(name: capitalName, country: self)
    }
}

class City {
    let name: String
    unowned let country: Country
    init(name: String, country: Country) {
        self.name = name
        self.country = country
    }
}
```

* A strong reference cycle can also occur if you assign a closure to a property of a class instance, and the body of that closure captures the instance.

* This strong reference cycle occurs because closures, like classes, are reference types. When you assign a closure to a property, you are assigning a reference to that closure.
  
* You resolve a strong reference cycle between a closure and a class instance by defining a `capture list` as part of the closure’s definition.

* Swift requires you to write self.someProperty or self.someMethod() (rather than just someProperty or someMethod()) whenever you refer to a member of self within a closure. This helps you remember that it’s possible to capture self by accident.

* Each item in a capture list is a pairing of the weak or unowned keyword with a reference to a class instance (such as self) or a variable initialized with some value (such as delegate = self.delegate!). These pairings are written within a pair of square braces, separated by commas.

## Reference

[Automatic Reference Counting](https://docs.swift.org/swift-book/LanguageGuide/AutomaticReferenceCounting.html)