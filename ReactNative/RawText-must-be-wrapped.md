# RawText must be wrapped issue

RawText " " must be wrapped in an explicit <Text> component.

This error happens when I put some codes in one line.

```
<View> <PageView /> </View>
```

And this issue is resolved by put this code in three lines.

```
<View>
  <PageView />
</View>
```
