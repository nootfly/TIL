# iOS Drawing cheat sheet

* The iOS native graphics system combines three major technologies: UIKit, Core Graphics, and Core Animation. UIKit provides views and some high-level drawing functionality within those views, Core Graphics provides additional (lower-level) drawing support within UIKit views, and Core Animation provides the ability to apply transformations and animation to UIKit views. Core Animation is also responsible for view compositing.

*  iOS provides two primary paths for creating high-quality graphics in your system: OpenGL or native rendering using Quartz, Core Animation, and UIKit.

* Quartz is the main drawing interface, providing support for path-based drawing, anti-aliased rendering, gradient fill patterns, images, colors, coordinate-space transformations, and PDF document creation, display, and parsing. UIKit provides Objective-C wrappers for line art, Quartz images, and color manipulations. Core Animation provides the underlying support for animating changes in many UIKit view properties and can also be used to implement custom animations.

* The default coordinate system used by the UIKit and Core Animation frameworks is ULO-based. The default coordinate system used by Core Graphics framework is LLO-based. The default coordinate system in OS X is LLO-based.

* One point does not necessarily correspond to one physical pixel.

* Native drawing technologies, such as Core Graphics, take the current scale factor into account for you. For example, if one of your views implements a drawRect: method, UIKit automatically sets the scale factor for that view to the screen’s scale factor. In addition, UIKit automatically modifies the current transformation matrix of any graphics contexts used during drawing to take into account the view’s scale factor. Thus, any content you draw in your drawRect: method is scaled appropriately for the underlying device’s screen.

* As a rule, lines that are an odd number of physical pixels wide appear softer than lines with widths measured in even numbers of physical pixels unless you adjust their position to make them cover pixels fully.

* In iOS, it is recommended that you use the UIKit functions for drawing to bitmap contexts and PDF contexts. However, if you do use the Core Graphics alternatives and intend to display the rendered results, you will have to adjust your code to compensate for the difference in default coordinate systems.

* Quartz is the general name for the native drawing technology in iOS. The Core Graphics framework is at the heart of Quartz, and is the primary interface you use for drawing content.

* If you only use UIKit methods and function for drawing, you shouldn’t need to flip the CTM. However, if you mix Core Graphics or Image I/O function calls with UIKit calls, flipping the CTM might be necessary.

* The key technology in Core Animation is the layer object. Layers are lightweight objects that are similar in nature to views, but that are actually model objects that encapsulate geometry, timing, and visual properties for the content you want to display.

* The UIBezierPath class is really just a wrapper for a CGPathRef data type and the drawing attributes associated with that path.

* Because a UIBezierPath object owns its underlying CGPathRef data type, you cannot simply retrieve that type and modify it directly. Instead, you must make a mutable copy, modify the copy, and then assign the copy back to the CGPath property.

*  The containsPoint: method and the Core Graphics hit-testing functions operate only on closed paths. These methods always return NO for hits on open subpaths. If you want to do hit detection on an open subpath, you must create a copy of your path object and close the open subpaths before testing points.



Reference: [Drawing and Printing Guide for iOS](https://developer.apple.com/library/content/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010156-CH1-SW1)
