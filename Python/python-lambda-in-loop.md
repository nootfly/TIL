# Python lambda in a loop

```python
funcs = []
for x in [1,2,3]:
  funcs.append(lambda: x)

for f in funcs:
  print f()

# output:
3
3
3
```

```python
def makeFunc(x):
  return lambda: x

funcs = []
for x in [1,2,3]:
  funcs.append(makeFunc(x))

for f in funcs:
  print f()

# output:
1
2
3
```

## Reference

[https://stackoverflow.com/questions/19837486/python-lambda-in-a-loop](https://stackoverflow.com/questions/19837486/python-lambda-in-a-loop)