# Python Code sippets

## date difference

`if (datetime.today() - yourdate).days == 0:`

## get string between two strings

```python
import re

s = 'asdf=5;iwantthis123jasd'
result = re.search('asdf=5;(.*)123jasd', s)
print(result.group(1))
```