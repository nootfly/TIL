# ARCHS[@]: unbound variable in Xcode 13.1

Open VSCode and go to directory ios/App/App.xcodeproj/project.pbxproj that file and perform a search EXCLUDED_ARCHS

`EXCLUDED_ARCHS = arm64; `

and delete everyline containing `EXCLUDED_ARCHS`

[https://stackoverflow.com/a/65775041](https://stackoverflow.com/a/65775041)

