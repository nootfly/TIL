# Android unit tests resources mock

```kotlin

    @Mock
    private lateinit var mockContextResources: Resources

    @Before
    fun init() {
        mockContextResources = mock()
        Mockito.`when`(mockContextResources.getString(ArgumentMatchers.anyInt())).thenReturn("mocked string")
    }

```

