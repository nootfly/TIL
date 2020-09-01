# Android code snippets

## Android switch - change background

[https://stackoverflow.com/a/28981942](https://stackoverflow.com/a/28981942)

## get application language and device language

```kotlin
val currentSysLocale = Resources.getSystem().getConfiguration().locales[0]
val currentAppLocale = Locale.getDefault().getLanguage()
Log.d("sys locale","$currentSysLocale")
Log.d("app locale","$currentAppLocale")
```

[https://stackoverflow.com/a/58611147](https://stackoverflow.com/a/58611147)

## Reuse layout

```xml
<layout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto">

    <data>
        <variable name="myText" type="java.lang.String"/>
        <variable name="mySrc" type="android.graphics.drawable.Drawable"/>
    </data>

    <LinearLayout>
        <TextView android:text="@{myText}"/>
        <ImageView android:src="@{mySrc}"/>
    </LinearLayout>
</layout>

<layout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto">

    <LinearLayout>
        <include layout="xxLayout"
            app:myText="@{`aaa`}"
            app:mySrc="@{@drawable/bbb}"/>
        <include layout="xxLayout"
            app:myText="@{`ccc`}"
            app:mySrc="@{@drawable/ddd}"/>
    </LinearLayout>
</layout>
```

[https://stackoverflow.com/a/52881294](https://stackoverflow.com/a/52881294)

## Remove border of buttons

```xml
style="?android:attr/borderlessButtonStyle"
```

## Email, phone, SMS intents

```kotlin
    private fun makeCall(phoneNum: String) {
        val callIntent = Intent(Intent.ACTION_DIAL)
        callIntent.data = Uri.parse("tel:" + Uri.encode(phoneNum.trim()))
        callIntent.flags = Intent.FLAG_ACTIVITY_NEW_TASK
        startActivity(callIntent)
    }

    private fun sendEmail(email: String) {
        val emailIntent = Intent(
            Intent.ACTION_SENDTO, Uri.fromParts(
                "mailto", email, null
            )
        )
        emailIntent.putExtra(Intent.EXTRA_SUBJECT, "Subject")
        emailIntent.putExtra(Intent.EXTRA_TEXT, "Body")
        startActivity(Intent.createChooser(emailIntent, "Send email..."))
    }

    private fun sendSMS(phoneNum: String) {

       val defaultSmsPackageName =
            Telephony.Sms.getDefaultSmsPackage(requireContext()) // Need to change the build to API 19
        val sendIntent = Intent(Intent.ACTION_SEND, Uri.parse("smsto: ${phoneNum.trim()}"))
        sendIntent.type = "text/plain"
        sendIntent.putExtra("sms_body", "")
        sendIntent.putExtra("address", phoneNum.trim())   //this line is key to set a number.
        if (defaultSmsPackageName != null) {
            sendIntent.setPackage(defaultSmsPackageName)
        }
        if (sendIntent.resolveActivity(requireActivity().packageManager) != null) {
            startActivity(sendIntent)
        }
    }
```

## `TextField` integer input type

```xml
android:inputType="numberSigned"
```

```kotlin
passwordText.inputType = InputType.TYPE_CLASS_NUMBER
```

[https://stackoverflow.com/a/24160385](https://stackoverflow.com/a/24160385)
