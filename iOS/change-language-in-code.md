# Programmatically change the app language

```swift
// set current language:
Language.setCurrentLanguage(languageAbbreviation)
UserDefaults.standard.set([languageAbbreviation], forKey: "AppleLanguages")
UserDefaults.standard.synchronize()
```


## References

[How to programmatically change the app language without restarting the app](https://www.codebales.com/how-programmatically-change-app-language-without-restarting-app)

[https://stackoverflow.com/questions/22061402/change-language-in-the-app-programmatically-in-ios](https://stackoverflow.com/questions/22061402/change-language-in-the-app-programmatically-in-ios)