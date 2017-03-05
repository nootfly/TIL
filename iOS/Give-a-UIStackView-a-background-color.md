# Give a UIStackView a background color

>You can't do this – UIStackView is a non-drawing view, meaning that drawRect() is never called and its background color is ignored. If you desperately want a background color, consider placing the stack view inside another UIView and giving that view a background color.


Reference: https://www.hackingwithswift.com/example-code/uikit/how-to-give-a-uistackview-a-background-color
