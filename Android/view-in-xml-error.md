# Getting Binary XML file line #141: Attempt to invoke virtual method 'boolean java.lang.String.equals(java.lang.Object)' on a null object reference

```xml
 <view
                android:layout_width="match_parent"
                android:layout_height="1dp"/>
```

Change view to View in the 4 or 5 places where it is lowercase in your xml

## Reference

[https://stackoverflow.com/a/43919403](https://stackoverflow.com/a/43919403)