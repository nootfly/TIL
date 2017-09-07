# Xcode debugging tips

1. Using `Debugger Commond` - `expression NSLog("Loading friends...")` is faster than `Log Message` in a breakpoint

2. Open the jump bar of the source editor and type, and you can search function names.

3. Add a `New Run Script Phase` to generate warning for `TODO` and `FIXME`

   ```
   TAGS="TODO:|FIXME:
   find "${SRCROOT}" \( -type f -name "*.swift" \) -print0 | xargs -0 egrep --with-filename --line-number --only-matching "($TAGS).*\$" | perl -p -e "s/($TAGS)/ warning: \$1/"
   ```

4. Use `expression gift.name = "Xbox"` to change a runtime value
