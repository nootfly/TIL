# How to use Low Power Mode in code

In iOS9. We can get Low Power Mode through NSProcessInfo. There are two ways to use it. The code is from
https://littlebitesofcocoa.com/192-being-a-good-low-power-mode-citizen?utm_campaign=iOS%2BDev%2BWeekly&utm_medium=web&utm_source=iOS_Dev_Weekly_Issue_238

1. Read Low Power Mode property
```
func userStoppedScrolling() {
  guard NSProcessInfo.processInfo().lowPowerModeEnabled == false else { return }
  gifView.beginPlaying()
}
```

2. Register the notification
```
NSNotificationCenter.defaultCenter()
  .addObserver(self,
    selector: "lowPowerModeChanged:",
    name: NSProcessInfoPowerStateDidChangeNotification,
    object: nil
  )
```
