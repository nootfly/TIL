# Layout cheat sheet

* All layouts are subclasses of the android.view.ViewGroup class. A view group is a type of view that can contain multiple views.

* A frame layout stacks views.

* android:layout_gravity lets you say where you want views to appear in their available space.

* android:gravity lets you say where you want the contents to appear inside a view.

* The radio group containing the radio buttons is a subclass of LinearLayout. You can use the same attributes with a radio group as you can with a linear layout.

* Constraint Layout minimum SDK should be API 19. (Android 4.4)

* Once you’ve added constraints to opposite sides of your view, you can control where it should be positioned relative to each side by changing its bias. This tells Android what the proportionate length of the constraint should be on either side of the view.

* Relative layouts and grid layouts have largely been superseded by the constraint layout.


Reference: Head First Android Development, 2nd Edition
