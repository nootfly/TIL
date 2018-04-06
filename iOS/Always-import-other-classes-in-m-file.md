>You should ALWAYS #import other classes in your .m file.

>If they happen to also be members of your class, you can forward declare them (by using the @class directive) in your .h file.

>The reason for doing this is because when you #import a .h file, you only want to import declarations, not definitions. By using @class and only #importing in .m files, you are a) reducing overhead and b) makes for cleaner code.

>The reasoning behind forward declarations in header files is that it avoids unnecessary dependencies. i.e. Imagine B.h forward declares A and B.m imports A.h. Then imagine C.m, D.m, E.m and F.m import B.h. After all this is done, A.h changes. Since A is only forward declared in B.h, only B.m needs to rebuild. Without forward declarations, C.m, D.m, E.m and F.m would all need to be rebuild if A changes


Reference: [https://stackoverflow.com/a/2770246](https://stackoverflow.com/a/2770246)