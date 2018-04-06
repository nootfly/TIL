# Print system font names

It's a quick way to get system font names. The code is from http://codewithchris.com/common-mistakes-with-adding-custom-fonts-to-your-ios-app/

Swift:
```swift
 for family: String in UIFont.familyNames
 {
            print("\(family)")
            for names: String in UIFont.fontNames(forFamilyName: family)
            {
                print("== \(names)")
            }
  }

```

Objective C
```objective-c
for (NSString* family in [UIFont familyNames])
{
    NSLog(@"%@", family);

    for (NSString* name in [UIFont fontNamesForFamilyName: family])
    {
        NSLog(@"  %@", name);
    }
}
```
