# iOS Keychain check sheet

*  A keychain is simply a database stored in the file system, and an iOS device has a single keychain that is available to all apps.

* In iOS, the keychain is automatically unlocked when the devices is unlocked.

* In macOS, if you make this call from the same app that created the keychain item, Keychain Services automatically grants access because the app is in the item’s ACL.

* In iOS, and in macOS when using the iCloud keychain (for items with the kSecAttrSynchronizable attribute set to kCFBooleanTrue), you share keychain items using Access Groups. This kind of sharing does not require interaction with, or permission from the user, but limits sharing to apps that are delivered by a single development team.

* Access Control Lists are not available in iOS or to macOS apps that use the iCloud keychain. For keychain item sharing in those environments, use Access Groups instead.

* Keychain does store values after we uninstall the app.

The content is from [Apple Keychain Services Programming Guide.](https://developer.apple.com/library/content/documentation/Security/Conceptual/keychainServConcepts/01introduction/introduction.html#//apple_ref/doc/uid/TP30000897-CH203-TP1)
