# Evenly distribute buttons across the width of an android linearlayout

```xml
<Space
        android:layout_width="0dp"
        android:layout_height="1dp"
        android:layout_weight="1" >
    </Space>

    <ImageButton
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:adjustViewBounds="true"
        android:background="@null"
        android:gravity="center_horizontal|center_vertical"
        android:src="@drawable/tars_active" />

    <Space
        android:layout_width="0dp"
        android:layout_height="1dp"
        android:layout_weight="1" >
    </Space>

    <ImageButton
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:adjustViewBounds="true"
        android:background="@null"
        android:gravity="center_horizontal|center_vertical"
        android:src="@drawable/videos_active" />

    <Space
        android:layout_width="0dp"
        android:layout_height="1dp"
        android:layout_weight="1" >
    </Space>
```

Reference: [https://stackoverflow.com/a/14125793/1146834]()

