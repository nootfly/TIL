# Handle Up navigation

override onSupportNavigateUp() to handle Up navigation

```kotlin

private lateinit var appBarConfiguration: AppBarConfiguration

...

override fun onCreate(savedInstanceState: Bundle?) {
    ...

    val navController = findNavController(R.id.nav_host_fragment)
    appBarConfiguration = AppBarConfiguration(navController.graph)
    setupActionBarWithNavController(navController, appBarConfiguration)
}

override fun onSupportNavigateUp(): Boolean {
    val navController = findNavController(R.id.nav_host_fragment)
    return navController.navigateUp(appBarConfiguration)
            || super.onSupportNavigateUp()
}
```

[https://developer.android.com/guide/navigation/navigation-ui#action_bar](https://developer.android.com/guide/navigation/navigation-ui#action_bar)
