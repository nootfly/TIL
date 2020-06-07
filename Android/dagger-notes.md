# Dagger notes

* When `@Inject` is annotated on a class constructor, it's telling Dagger how to provide instances of that class. When it's annotated on a class field, it's telling Dagger that it needs to populate the field with an instance of that type.

* Use `@Binds` to tell Dagger which implementation it needs to use when providing an interface. @Binds must annotate an abstract function.

* Use `@BindsInstance` for objects that are constructed outside of the graph (e.g. instances of Context).

* Important: When using Activities, inject Dagger in the Activity's `onCreate` method before calling `super.onCreate` to avoid issues with fragment restoration. In `super.onCreate`, an Activity during the restore phase will attach fragments that might want to access activity bindings.

* Important: Dagger-injected fields **cannot be private**. They need to have at least package-private visibility.

* Use Scopes to have a unique instance of a type in a Component. This is what is also called "to scope a type to the Component's lifecycle". Scoping a type to a Component means that the same instance of that type will be used every time the type needs to be provided.

* `Subcomponents` are components that inherit and extend the object graph of a parent component. Thus, all objects provided in the parent component will be provided in the subcomponent too. In this way, an object from a subcomponent can depend on an object provided by the parent component.

* Scoping rules:

    When a type is marked with a scope annotation, it can only be used by Components that are annotated with the same scope.
    When a Component is marked with a scope annotation, it can only provide types with that annotation or types that have no annotation.
    A subcomponent cannot use a scope annotation used by one of its parent Components.

    Components also involve subcomponents in this context.

* The return type of the `@Provides` function (it doesn't matter how it's called) tells Dagger what type is added to the graph. The parameters of that function are the dependencies that Dagger needs to satisfy before providing an instance of that type.

* You can use the `@Provides` annotation in Dagger modules to tell Dagger how to provide:

  * Implementations of an interface (although `@Binds` is recommended because it generates less code and therefore it's more efficient).
   * Classes that your project doesn't own (e.g. instances of `Retrofit`).

* A **qualifier** is a custom annotation that will be used to identify a dependency.

```kotlin
@Retention(AnnotationRetention.BINARY)
@Qualifier
annotation class RegistrationStorage

@Retention(AnnotationRetention.BINARY)
@Qualifier
annotation class LoginStorage

@Module
class StorageModule {

    @RegistrationStorage
    @Provides
    fun provideRegistrationStorage(context: Context): Storage {
        return SharedPreferencesStorage("registration", context)
    }

    @LoginStorage
    @Provides
    fun provideLoginStorage(context: Context): Storage {
        return SharedPreferencesStorage("login", context)
    }
}
```

* You can achieve the same functionality as **qualifiers** with the `@Named` annotation, however **qualifiers** are recommended because:

    * They can be stripped out from Proguard or R8
    * You don't need to keep a shared constant for matching the names
    * They can be documented


## References

[Using Dagger in your Android app - Kotlin Codelab](https://codelabs.developers.google.com/codelabs/android-dagger/index.html#0)

[Dependency injection in Android](https://developer.android.com/training/dependency-injection)

[Manual dependency injection](https://developer.android.com/training/dependency-injection/manual)

[Dagger basics](https://developer.android.com/training/dependency-injection/dagger-basics)
