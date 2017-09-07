# Gradle damon error

You can solve the below issue by add `org.gradle.jvmargs=-Xmx1024m` in `gradle.properties` file.

>Error:Unable to start the daemon process.
>This problem might be caused by incorrect configuration of the daemon.
>For example, an unrecognized jvm option is used.
>Please refer to the user guide chapter on the daemon at https://docs.gradle.org/3.3/userguide/gradle_daemon.html
>Please read the following process output to find out more:

Reference:
[https://stackoverflow.com/a/34734684](https://stackoverflow.com/a/34734684)