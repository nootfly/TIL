# Hilt DI notes

* A container is a class which is in charge of providing dependencies in your codebase and knows how to create instances of other types of your app. It manages the graph of dependencies required to provide those instances by creating them and managing their lifecycle.

   A container exposes methods to get instances of the types it provides. Those methods can always return a different instance or the same instance. If the method always provides the same instance, we say that the type is scoped to the container.

* `@HiltAndroidApp` triggers Hilt's code generation including a base class for your application that can use dependency injection. The application container is the parent container of the app, which means that other containers can access the dependencies that it provides.

* Hilt currently supports the following Android types: Application (by using `@HiltAndroidApp`), Activity, Fragment, View, Service and BroadcastReceiver.

  Hilt only supports activities that extend `FragmentActivity` (like `AppCompatActivity`) and fragments that extend the Jetpack library Fragment, not the (now deprecated) Fragment from the Android platform.

* **Warning**: Hilt does not support retained fragments.

* To perform field injection, use the @Inject annotation on Android classes' fields you want to be provided (or injected) by Hilt. **Warning**: Fields injected by Hilt cannot be private.

* if you want an activity container to always provide the same instance of a type, you can annotate that type with `@ActivityScoped`.

* Bindings available in containers higher up in the hierarchy, are also available in lower levels of the hierarchy.

* **Modules are used to add bindings to Hilt**, or in other words, to tell Hilt how to provide instances of different types. In Hilt modules, you include bindings for **types that cannot be constructor** injected such as interfaces or classes that are not contained in your project. An example of this is OkHttpClient - you need to use its builder to create an instance.

* **A Hilt module is a class annotated with `@Module` and `@InstallIn`**. `@Module` tells Hilt this is a module and `@InstallIn` tells Hilt in which containers the bindings are available by specifying a Hilt Component. You can think of a Hilt Component as a container.

* **For each Android class that can be injected by Hilt, there's an associated Hilt Component**. For example, the `Application` container is associated with `ApplicationComponent`, and the `Fragment` container is associated with `FragmentComponent`.

* In Kotlin, modules that only contain `@Provides` functions can be `object` classes. In this way, providers get optimized and almost in-lined in generated code.

* Each Hilt container comes with a set of default bindings that can be injected as dependencies into your custom bindings. This is the case of the `applicationContext:` to access it, you need to annotate the field with `@ApplicationContext`.

* **To tell Hilt what implementation to use for an interface, you can use the @Binds annotation on a function inside a Hilt module.**

* `@Binds` must annotate an abstract function (since it's abstract, it doesn't contain any code and the class needs to be abstract too). The return type of the abstract function is the interface we want to provide an implementation for (i.e. `AppNavigator`). The implementation is specified by adding a unique parameter with the interface implementation type (i.e. `AppNavigatorImpl`).

* Hilt Modules cannot contain both non-static and abstract binding methods, so you cannot place `@Binds` and `@Provides` annotations in the same class.

* **To tell Hilt how to provide different implementations (multiple bindings) of the same type, you can use qualifiers.** A qualifier is an annotation used to identify a binding.

* **Testing with Hilt requires no maintenance because Hilt automatically generates a new set of components for each test.**

* An entry point is the boundary place where you can get Hilt-provided objects from code that cannot use Hilt to inject its dependencies. It is the point where code first enters into containers managed by Hilt.
