# Xcode constantly crashing

To solve this issue:

```sh
defaults delete com.apple.dt.Xcode
rm -rf $HOME/Library/Application Support/Developer/Shared/Xcode
rm -rf $HOME/Library/Saved\ Application\ State/com.apple.dt.Xcode.savedState
rm -rf $HOME/Library/Preferences/com.apple.dt.Xcode.*
```

## Reference

[Reverting all Xcode settings to their original state](https://stackoverflow.com/a/31719350)