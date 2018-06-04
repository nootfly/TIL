#RecyclerView laggy scrolling issue

When using RecycelerView inside NestedScrollView, recyclerView scroolling is laggy. To solve this issue, just set:

```kotlin
   recyclerView.isNestedScrollingEnabled = false
```

Reference: [https://stackoverflow.com/questions/37301724/recyclerview-inside-nested-scrollview-scroll-but-does-not-fast-scroll-like-norma/37337641#37337641](https://stackoverflow.com/questions/37301724/recyclerview-inside-nested-scrollview-scroll-but-does-not-fast-scroll-like-norma/37337641#37337641)
