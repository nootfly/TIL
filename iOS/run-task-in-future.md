# Performing a Task in the Future

Use asyncAfter to schedule a closure of code to run in the future:

```swfit
// Place a bomb, but make it explode in 10 seconds
PlaceBomb()

let deadline = DispatchTime.now() + 10

DispatchQueue.main.asyncAfter(deadline: deadline, execute: {
    // Time's up. Kaboom.
    ExplodeBomb()
})
```

GCD provides a function called dispatch_after that runs a closure on an operation queue at a given time.

```objective c
int parameter1 = 12;
float parameter2 = 144.1;

// Delay execution of my block for 10 seconds.
dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 10 * NSEC_PER_SEC), dispatch_get_main_queue(), ^{
    NSLog(@"parameter1: %d parameter2: %f", parameter1, parameter2);
});
```

## Reference

[https://developer.apple.com/documentation/dispatch/1452876-dispatch_after](https://developer.apple.com/documentation/dispatch/1452876-dispatch_after)
