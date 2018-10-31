# iBeacons cheat sheet

* The human body itself is an excellent attenuator of
Bluetooth signals. Simply having your back to a beacon (i.e.
where your body is positioned between the device and the
beacon) will affect the signal strength and thereby lower the
accuracy.

* Similar to the existing geofence region monitoring, an
application can request notifications when a device enters
or leaves a region defined by a beacon. When an
application makes this request to begin monitoring a
beacon region it must specify the UUID of the iBeacon
advertisement. While an app is limited to 20 regions being
monitored, by using a single UUID in multiple locations, a
device can easily monitor many physical locations
simultaneously.

* In addition to the UUID, an application can optionally supply the major and minor fields to
further specify a beacon region to be monitored.

* As with the existing region monitoring, when the user enters or exits the beacon region, the
application will be notified. If the application is not currently running (for example, if it was
terminated due to memory pressure on the device), then the application is launched in the
background and the notification delivered. One important consideration is in iOS 7 if the user
explicitly disallows Background App Refresh (either globally or specifically for your app) then
your app will no longer receive region monitoring notifications. It can continue to use the
ranging APIs, however.

* iOS 7 introduces a new set of APIs for determining the approximate proximity to a device using
iBeacon technology, a process known as “ranging”

* Passbook passes can take advantage of devices with iBeacon technology as well. By including
the UUID of beacon, a Passbook pass can be made relevant when it is in the beacon’s region.
This works the same way specifying latitude and longitude values in the locations array of
your pass. You can specify the UUID and, optionally, the major and minor values as an array in
the beacons key for your pass.

* To provide the best user experience, it is critical to perform calibration in your deployment
environment. As each beacon is installed you should perform a calibration step. Core Location
uses an estimation model that requires calibration at a distance of 1 meter away from the
beacon.

* Ranging API are not expected to be used in the background. For best results, ranging should
be used when your app is frontmost and the user is interacting with your app.

* Due to the issues around signal strength and the variabilities in deployment environments,
iBeacon technology is not intended to be used for specific location identification. It should
be capable of providing room-level accuracy, but there are many factors that need to be
considered to build a successful deployment.

* For an iOS device to issue iBeacon advertisements , the app requesting this functionality
must be frontmost, with the screen turned on and the device unlocked.

* Turning an iOS Device into an iBeacon
   1. Obtain or generate a 128-bit UUID for your device.

   2. Create a CLBeaconRegion object containing the UUID value along with appropriate major and minor values for your beacon.

   3. Advertise the beacon information using the Core Bluetooth framework.

## References

[Getting Started with iBeacon](https://developer.apple.com/ibeacon/Getting-Started-with-iBeacon.pdf)

[Turning an iOS Device into an iBeacon](https://developer.apple.com/documentation/corelocation/turning_an_ios_device_into_an_ibeacon)