# MacBook disk / SSD health

To check **MacBook disk / SSD health**, use these methods:

## 1. Check in Disk Utility

1. Open **Disk Utility**
2. Click **View → Show All Devices**
3. Select the **physical internal disk** at the top, not just “Macintosh HD”
4. Look for **S.M.A.R.T. Status**

You want to see:

> **S.M.A.R.T. Status: Verified**

If it says **Failing**, back up immediately.

## 2. Check using Terminal

Open **Terminal** and run:

```bash
diskutil info disk0 | grep SMART
```

You may see something like:

```bash
SMART Status: Verified
```

For Apple Silicon Macs, the internal SSD is usually `disk0`.

## 3. Check detailed SSD wear using smartmontools

macOS built-in tools only show basic health. For more detail, install smartmontools:

```bash
brew install smartmontools
```

Then run:

```bash
smartctl -a disk0
```

Or:

```bash
smartctl -a /dev/disk0
```

Look for things like:

```text
Percentage Used
Data Units Written
Media and Data Integrity Errors
Critical Warning
```

Important signs:

| Item             |              Good |                  Bad |
| ---------------- | ----------------: | -------------------: |
| Critical Warning |                 0 |        anything else |
| Media Errors     |                 0 |    increasing number |
| Percentage Used  |        low number | close to or over 100 |
| SMART overall    | PASSED / Verified |     FAILED / Failing |

## 4. Check free space

Low free space can make the Mac slow and increase SSD pressure.

Go to:

**Apple menu → System Settings → General → Storage**

Try to keep at least **15–20% free space**.

## 5. Best simple check

Run this first:

```bash
diskutil info disk0 | grep -i smart
```

If it says **Verified**, your disk is probably okay.

Then check storage:

```bash
df -h /
```

If your SSD is almost full, clean up files before worrying about hardware failure.
