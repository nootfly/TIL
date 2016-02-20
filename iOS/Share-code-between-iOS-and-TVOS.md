# Share code between iOS and TVOS

Using CocoaPods different targets is a way to share code between iOS and TVOS.
The code is from https://labs.ribot.co.uk/sharing-functionality-across-tvos-and-ios-228c76b03a06#.4pa6trgb7.

```
# Podfile
source 'https://github.com/CocoaPods/Specs.git'

def shared_pods
    pod 'Alamofire', '~> 3.0'
    pod 'AlamofireImage', '~> 2.0'
end

target 'ribotTeam' do
    platform :ios, '9.0'
    use_frameworks!
    shared_pods
end

target 'ribotTeamtvOS' do
    platform :tvos, '9.0'
    use_frameworks!
    shared_pods
end
```
