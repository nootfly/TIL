# Fragment removal animation

```kotlin
            val animation = AnimationUtils.loadAnimation(activity, R.anim.bottom_down)
            animation.duration = 500
            animation.setAnimationListener(object : Animation.AnimationListener {
                override fun onAnimationEnd(animation: Animation) {
                    try {
                        val ft = fragmentManager.beginTransaction()
                        ft.remove(this@CurrentFragment)
                        ft.commitAllowingStateLoss()
                    } catch (e: Exception) {
                        e.printStackTrace()
                    }

                }

                override fun onAnimationRepeat(p0: Animation?) {

                }

                override fun onAnimationStart(p0: Animation?) {

                }
            })

            //Start the animation.
            getView()!!.startAnimation(animation)
```

## Reference

[https://stackoverflow.com/a/18170013](https://stackoverflow.com/a/18170013)