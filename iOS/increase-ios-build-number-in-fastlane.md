# increase iOS build number in Fastlane

There are two steps to do this.

1. Enable agvtool in Xcode according to [https://developer.apple.com/library/content/qa/qa1827/_index.html](https://developer.apple.com/library/content/qa/qa1827/_index.html)

2. Call `increment_build_number` function in `Fastfile`.
