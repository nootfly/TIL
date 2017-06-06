# OpenGL cheat sheet


* OpenGL ES is a C-based API. The OpenGL ES specification does not define a windowing layer

* Apps that are running in the background may not call OpenGL ES functions. If your app accesses the graphics processor while it is in the background, it is automatically terminated by iOS.

* Although the context holds the OpenGL ES state, it does not directly manage OpenGL ES objects. Instead, OpenGL ES objects are created and maintained by an EAGLSharegroup object. Every context contains an EAGLSharegroup object that it delegates object creation to.

* All contexts associated with the same sharegroup must use the same version of the OpenGL ES API as the initial context.

* The GLKView class manages OpenGL ES infrastructure to provide a place for your drawing code, and the GLKViewController class provides a rendering loop for smooth animation of OpenGL ES content in a GLKit view.

* The three steps for drawing OpenGL ES content: preparing OpenGL ES infrastructure, issuing drawing commands, and presenting the rendered content to Core Animation for display.
