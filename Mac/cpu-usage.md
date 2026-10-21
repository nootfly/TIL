A few built-in commands for checking CPU usage on a Mac:

**1. `top`**: live view, sorted by CPU
```bash
top -o cpu
```
Press `q` to quit. The header line `CPU usage: x% user, y% sys, z% idle` shows overall load.

**2. One snapshot of overall CPU usage** (no live screen)
```bash
top -l 1 | grep "CPU usage"
```

**3. Top 10 processes by CPU**
```bash
ps -Ao pid,pcpu,pmem,comm -r | head -n 11
```
`-r` sorts by CPU, highest first.

**4. Load averages** (1, 5 and 15 minutes)
```bash
uptime
```

**5. Per-core detail, power and frequency** (needs admin rights)
```bash
sudo powermetrics --samplers cpu_power -i 1000 -n 1
```

**Optional: `htop`** gives a nicer, color-coded interactive view. Install it with Homebrew:
```bash
brew install htop
```

For a quick check, `top -o cpu` is usually enough.