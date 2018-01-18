# Command /bin/sh failed with exit code 1

I run into some issues about compilation.

1. `Command /bin/sh failed with exit code 1`
    
   After I upgraded xCode, and I could run my app on a simulator, but I cannot run it on a device. This issue was resolved after I restarted my Mac.

2. `ld: framework not found`

   I got this issue when I added some frameworks to `project -> targets -> general -> Embedded Binaries` and I added them to `project -> targets -> Build Phases -> Link Binary With Libraries`. I solved this issue by removing them from `Link Binary With Libraries`.
