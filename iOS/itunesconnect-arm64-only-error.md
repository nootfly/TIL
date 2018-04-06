# Fix iTunesConnect must have an arm64-only executable error

When you upload your app to iTunesConnect, you may meet "must have an arm64-only executable" error. To solve this issue, you need to update your `Valid Architectures` to `arm64` in Xcode target `Build Settings`.
