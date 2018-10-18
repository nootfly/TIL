# Xcode 10 (iOS 12) does not contain libstdc++6.0.9

>libstdc++ was deprecated 5 years ago. Apple's more recent platforms (tvOS and watchOS) don't support it.

>Support was removed from the iOS 12.0 Simulator runtime, but it remains in the iOS 12.0 (device) runtime for binary compatibility with shipping apps.

>You should update your project to use libc++ rather than libstdc++ by setting the CLANG_CXX_LIBRARY build setting ("C++ Standard Library") to libc++.

Xcode 10 cancels the libstdc++ library with built-in the lib so we should copy the file to the lib by hand.

copy the file: (libstdc++.6.0.9.tbd) and (libstdc++.6.tbd) to :

`/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk/usr/lib`

and 

`/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator.sdk/usr/lib`

## References

[https://stackoverflow.com/a/52416822](https://stackoverflow.com/a/52416822)

[libstdc-.6.0.9.tbd](https://github.com/Kila2/libstdc-.6.0.9.tbd)