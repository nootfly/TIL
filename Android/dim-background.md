# Dim background

for API 18+

```kotlin
fun applyDim(@NonNull parent: ViewGroup, dimAmount: Float) {
            val dim = ColorDrawable(Color.BLACK)
            dim.setBounds(0, 0, parent.width, parent.height)
            dim.alpha = (255 * dimAmount).toInt()

            val overlay = parent.overlay
            overlay.add(dim)
        }

        fun clearDim(@NonNull parent: ViewGroup) {
            val overlay = parent.overlay
            overlay.clear()
        }
```

## Reference

[https://stackoverflow.com/a/29950606](https://stackoverflow.com/a/29950606)