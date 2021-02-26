# Clean simulators

```shell
echo "Shutting down the simulator app"
osascript -e 'quit app "Simulator"'

echo "Making sure ALL simulators are shutdown"
xcrun simctl list | grep Booted | grep -e "[0-9A-F\-]\{36\}" -o | xargs xcrun simctl shutdown

echo "Erasing apps from all simulators and resetting back to clean state"
xcrun simctl erase all

echo "Killing com.apple.CoreSimulator.CoreSimulatorService"
killall -9 com.apple.CoreSimulator.CoreSimulatorService

```

[https://github.com/fastlane/fastlane/issues/6968#issuecomment-301565217](https://github.com/fastlane/fastlane/issues/6968#issuecomment-301565217)
