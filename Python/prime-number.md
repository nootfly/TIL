# Python Prime number checker

```python
import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
```

## Reference

[https://stackoverflow.com/a/18833870](https://stackoverflow.com/a/18833870)