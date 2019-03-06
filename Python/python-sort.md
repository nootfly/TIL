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

class Interval:
    def __init__(self, left, right):
        self.left, self.right = left, right

    def __repr__(self):
        return "Interval(%d, %d)" % (self.left, self.right)


data = [(3, 2), (3, 1), (2, 7), (1, 5), (2, 6), (1, 7)]
intervals = [Interval(left, right) for left, right in data]

print(sorted(intervals, key=lambda i: (i.left, i.right)))  
# Result: [Interval(1, 5), Interval(1, 7), Interval(2, 6), Interval(2, 7), Interval(3, 1), Interval(3, 2)]

print(sorted(intervals, key=lambda i: (-i.left, i.right)))
# Result: [Interval(3, 1), Interval(3, 2), Interval(2, 6), Interval(2, 7), Interval(1, 5), Interval(1, 7)]

print(sorted(intervals, key=lambda i: (i.right, i.left)))
# Result: [Interval(3, 1), Interval(3, 2), Interval(1, 5), Interval(2, 6), Interval(1, 7), Interval(2, 7)]

print(sorted(intervals, key=lambda i: (-i.right, i.left)))
# Result: [Interval(1, 7), Interval(2, 7), Interval(2, 6), Interval(1, 5), Interval(3, 2), Interval(3, 1)]
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