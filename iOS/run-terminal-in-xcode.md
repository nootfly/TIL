#  Open terminal window from Xcode

1. Create executable shell script with the following contents and save it anywhere

```
    #!/bin/bash
    open -a Terminal "`pwd`"
```

2. Add execute permissions to your script: $ chmod +x <YourShellScript>
3.  In the Xcode menu bar, Go to Xcode -> Preferences -> Behaviors.
4. Add a Custom behavior
5. Name it "Open Terminal", or whatever.
6. (Optional) Configure a hotkey for the behavior by tapping on the ⌘
7. (Optional) Input hotkey combination
8. Checkmark Run, select you script from step 1.
9. Use it From Xcode -> Behaviors.

[https://stackoverflow.com/a/41429508](https://stackoverflow.com/a/41429508)