# Netlify Firebase authentication redirect issue

When you see `Looks like you've followed a broken link or entered a URL that doesn't exist on this site.`, you can add the following code in your `index.html head`

```html
<base href="/">
<!-- This must come before the css and javascripts -->
```

## Reference

[https://stackoverflow.com/a/49599043](https://stackoverflow.com/a/49599043)