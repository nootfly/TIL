# Python objects sort

## Method 1

```python
def IntervalKey(interval):
    return interval.left

A = []
A.append(Interval(1, 7))
A.append(Interval(5, 6))
A.append(Interval(3, 4))
A.sort(key=IntervalKey)
```

## Method 2

```python
class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right


    def __lt__(self, other):
        return self.left < other.left
```