#  pprint — Data pretty printer

`pprint` contains a “pretty printer” for producing aesthetically pleasing representations of your data structures.

```python
data = [ (i, { 'a':'A',
               'b':'B',
               'c':'C',
               'd':'D',
               'e':'E',
               'f':'F',
               'g':'G',
               'h':'H',
               }) for i in range(3)
         ]

from pprint import pprint


print('PRINT:')
print(data)
print()
print('PPRINT:')
pprint(data)
```

## References

[pprint — Data pretty printer](https://docs.python.org/2/library/pprint.html)

[pprint – Pretty-print data structures](https://pymotw.com/2/pprint/)