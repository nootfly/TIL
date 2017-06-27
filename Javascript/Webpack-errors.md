# Webpack errors

1. Error: Cannot find module 'webpack'

  ```
    npm install --save-dev webpack
   ```

2. configuration.output.path: The provided value "dist/assets" is not an absolute path!
  To solve this issue, you can add `__dirname` to a ouput path.

   ```
     output: {
        path: __dirname + "dist/assets",
        filename: "bundle.js",
        sourceMapFilename: 'bundle.map'
     }
    ```
