# Check mobile safari

```javascript
var ua = window.navigator.userAgent;
var iOS = !!ua.match(/iPad/i) || !!ua.match(/iPhone/i);
var webkit = !!ua.match(/WebKit/i);
var iOSSafari = iOS && webkit && !ua.match(/CriOS/i);
```

## Reference

[https://stackoverflow.com/a/29696509](https://stackoverflow.com/a/29696509)