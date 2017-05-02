# Quartz 2D cheat sheet

* You can think of a graphics context as a drawing destination, as shown in Figure 1-2. When you draw with Quartz, all device-specific characteristics are contained within the specific type of graphics context you use. In other words, you can draw the same image to a different device simply by providing a different graphics context to the same sequence of Quartz drawing routines. You do not need to perform any device-specific calculations; Quartz does it for you.

* A layer context (CGLayerRef) is an offscreen drawing destination associated with another graphics context. It is designed for optimal performance when drawing the layer to the graphics context that created it. A layer context can be a much better choice for offscreen drawing than a bitmap graphics context.

* The graphics context contains a stack of graphics states. When Quartz creates a graphics context, the stack is empty. When you save the graphics state, Quartz pushes a copy of the current graphics state onto the stack. When you restore the graphics state, Quartz pops the graphics state off the top of the stack. The popped state becomes the current graphics state.

* Quartz accomplishes device independence with a separate coordinate system—user space—mapping it to the coordinate system of the output device—device space—using the current transformation matrix, or CTM.

* In iOS, if you use a UIImage object to wrap a CGImage object you create, you do not need to modify the CTM. The UIImage object automatically compensates for the modified coordinate system applied by UIKit.

* f you create or copy an object, you own it, and therefore you must release it. That is, in general, if you obtain an object from a function with the words “Create” or “Copy” in its name, you must release the object when you’re done with it. Otherwise, a memory leak results.

* A PDF graphics context in iOS uses the default coordinate system provided by Quartz, without applying a transform to match the UIKit coordinate system. If your application plans on sharing drawing code between your PDF graphics context and the graphics context provided by UIView object, your application should modify the CTM of the PDF graphics context to modify the coordinate system

*  iOS applications should use the function UIGraphicsBeginImageContextWithOptions instead of using the low-level Quartz functions to create a bitmap graphics context.

* Path creation and path painting are separate tasks. Subpaths are built from lines, arcs, and curves.

* Points are x and y coordinates that specify a location in user space. You can call the function CGContextMoveToPoint to specify a starting position for a new subpath. Quartz keeps track of the current point, which is the last location used for path construction.

*  An empty path has no current point; you must call CGContextMoveToPoint to set the starting point for the first subpath or call a convenience function that implicitly does this for you.

* When you want to close the current subpath within a path, call the function CGContextClosePath to connect a segment to the starting point of the subpath. Subsequent path calls begin a new subpath, even if you do not explicitly set a new starting point.

* You must call a painting function to fill or stroke the path because creating a path does not draw the path.

* Quartz provides two data types for creating reusable paths—CGPathRef and CGMutablePathRef.

* iOS does not support device-independent or generic color spaces. iOS applications must use device color spaces instead.



Reference: [Quartz 2D Programming Guide](https://developer.apple.com/library/content/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html)
