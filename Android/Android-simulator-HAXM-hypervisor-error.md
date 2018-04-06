# Android simulator HAXM hypervisor error

If you see the below error on a mac when you start a android simulator, you can try to stop all virtual box instances and docker, and upgrade VirtualBox to the latest version.

`emulator: ERROR: Unfortunately, there's an incompatibility between HAXM hypervisor and VirtualBox 4.3.30+ which doesn't allow multiple hypervisors to co-exist.  It is being actively worked on; you can find out more about the issue at http://b.android.com/197915`
