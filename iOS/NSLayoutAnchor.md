# NSLayoutAnchor

> UIView does not provide anchor properties for the layout margin attributes. Instead, the layoutMarginsGuide property provides a UILayoutGuide object that represents these margins. Use the guide’s anchor properties to create your constraints.

These are the available layout anchors for UIView:

* widthAnchor
* heightAnchor
* topAnchor
* bottomAnchor
* leadingAnchor
* trailingAnchor
* leftAnchor
* rightAnchor
* centerXAnchor
* centerYAnchor
* firstBaselineAnchor
* lastBaselineAnchor


   ```
   // Creating constraints using NSLayoutConstraint
NSLayoutConstraint(item: subview,
                   attribute: .Leading,
                   relatedBy: .Equal,
                   toItem: view,
                   attribute: .LeadingMargin,
                   multiplier: 1.0,
                   constant: 0.0).active = true

NSLayoutConstraint(item: subview,
                   attribute: .Trailing,
                   relatedBy: .Equal,
                   toItem: view,
                   attribute: .TrailingMargin,
                   multiplier: 1.0,
                   constant: 0.0).active = true


// Creating the same constraints using Layout Anchors
let margins = view.layoutMarginsGuide

subview.leadingAnchor.constraintEqualToAnchor(margins.leadingAnchor).active = true
subview.trailingAnchor.constraintEqualToAnchor(margins.trailingAnchor).active = true

// Create & Add Layout Constraint
let leadingConstraint = subview.leadingAnchor.constraintEqualToAnchor(superview.leadingAnchor, constant: 8.0)

// Activate Layout Constraint
leadingConstraint.active = true

centerXAnchor.constraint(equalTo: (superview?.centerXAnchor)!, constant: 0).isActive = true

centerYAnchor.constraint(equalTo: (superview?.centerYAnchor)!, constant: 0).isActive = true

```


Reference: https://developer.apple.com/reference/uikit/nslayoutanchor
