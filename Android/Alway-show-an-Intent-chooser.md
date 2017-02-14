# Alway show an `Intent` chooser

If you want to alway show a chooser dialog, you can create `Intent` using `createChooser()`

   ```
   Intent intent = new Intent(Intent.ACTION_SEND);


    // Always use string resources for UI text.
    // This says something like "Share this photo with"
    String title = getResources().getString(R.string.chooser_title);
    // Create intent to show chooser
    Intent chooser = Intent.createChooser(intent, title);

    // Verify the intent will resolve to at least one activity
    if (intent.resolveActivity(getPackageManager()) != null) {
        startActivity(chooser);
    }
```
