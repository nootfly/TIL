# UITapGestureRecognizer or touchesBegan

`UITapGestureRecognizer` is a discrete gesture recognizer, and therefore never transitions to the began or changed states.
To animate a touch on a view, the good way is to use `touchesBegan` and `touchesEnded`

```objective-c
- (void)touchesBegan:(NSSet<UITouch *> *)touches withEvent:(UIEvent *)event {
    UITouch *touch= [touches anyObject];
    if ([touch view].superview == self.giftView){
        [UIView animateWithDuration:0.2  animations:^{
            self.giftView.transform = CGAffineTransformMakeScale(1.05, 1.05);
        } completion:nil];
    }
  }
```
