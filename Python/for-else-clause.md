# for else clause

> for loops also have an else clause which most of us are unfamiliar with. The else clause executes after the loop completes normally. This means that the loop did not encounter a break statement. 

```
for item in container:
    if search_something(item):
        # Found it!
        process(item)
        break
else:
    # Didn't find anything..
    not_found_in_container()
```

## Reference

[http://book.pythontips.com/en/latest/for_-_else.html](http://book.pythontips.com/en/latest/for_-_else.html)