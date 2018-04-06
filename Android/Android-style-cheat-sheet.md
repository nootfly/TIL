# Android style cheat sheet

* Prior to version 24.2.0, the Support Libraries prefixed with v4 could be used with API level 4 and above, and those prefixed with v7 could be used with API level 7 and above. When version 24.2.0 of the Support Libraries was released, the minimum API for all Support Libraries became API level 9. The minimum API level is likely to increase in the future.

* When you want to apply a theme to your app, you have two main options:
  1. Hardcode the theme in AndroidManifest.xml.
  2. Apply the theme using a style.

* `name="colorPrimary"` refers to the main color you want to use for your app. This color gets used for your app bar, and to “brand” your app with a particular color.

* `name="colorPrimaryDark"` is a darker variant of your main color. It gets used as the color of the status bar.

* `name="colorAccent"` refers to the color of any UI controls such as editable text views or checkboxes.

* How to add a toolbar
  1. Add the v7 AppCompat Support Library as a dependency.
  2. Make sure your activity extends the AppCompatActivity class.
  3. Remove the existing app bar.
  4. Add a toolbar to the layout.
  5. Update the activity to set the toolbar as the activity’s app bar.

 * A theme overlay is a special type of theme that alters the current theme by overwriting some of its attributes. 

 * To get the toolbar to behave like an app bar, we need to call the AppCompatActivity’s setSupportActionBar() method in the activity’s onCreate() method, which takes one parameter: the toolbar you want to set as the activity’s app bar.

 * How to add an action to an app bar
   1. Add resources for the action’s icon and text.
   2. Define the action in a menu resource file.
   3. Get the activity to add the menu resource to the app bar.
   4. Add code to say what the action should do when clicked.

 * Use the Back button to navigate back to the previous activity. Use the Up button to navigate up the app’s hierarchy.

  ```java
  ActionBar actionBar = getSupportActionBar();
  actionBar.setDisplayHomeAsUpEnabled(true);
  ```

 * Up button for an activity, you MUST specify its parent. If you don’t, you’ll get a null pointer exception when you call the setDisplayHomeAsUpEnabled() method. 

  

Refenece: Head First Android Development, 2nd Edition
