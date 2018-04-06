# CALayer shadow performance issue

Using ```shadowPath``` property can greatly improve performance.
http://stackoverflow.com/questions/7746921/iphone-animations-performance-is-very-poor-when-views-shadow-is-on



```objective-c
theView.layer.shadowPath = [UIBezierPath bezierPathWithRect:theView.bounds].CGPath;
```

Or

```objective-c
theView.layer.shadowPath = [UIBezierPath bezierPathWithRoundedRect:theView.bounds cornerRadius:theView.layer.cornerRadius].CGPath;
```
