# Android Activity lifecycle

* onStart() gets called when your activity becomes visible to the user.

* onSaveInstanceState() gets called before onStop().

* onRestart() gets called after your activity has been made invisible, before it gets made visible again.

* When you override any activity lifecycle method in your activity, you need to call the Activity superclass method. If you don’t, you’ll get an exception.

* An activity has a state of paused if it’s lost the focus but is still visible to the user. The activity is still alive and maintains all its state information.

* An activity has a state of paused if it’s lost the focus but is still visible to the user. The activity is still alive and maintains all its state information.

* If the activity becomes visible to the user again, the onRestart() method gets called, followed by onStart() and onResume().

* As the activity moves from running to destroyed, the onPause() and onStop() methods get called before the activity is destroyed.

* If you have an activity that’s visible, but never in the foreground and never has the focus, the onPause() and onResume() methods never get called.



Refenece: Head First Android Development, 2nd Edition