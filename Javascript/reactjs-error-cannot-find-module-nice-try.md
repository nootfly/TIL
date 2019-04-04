# Resolve Cannot find modlue 'nice-try' error

When running `yarn build` in a ReactJs web project directory

```javascript
internal/modules/cjs/loader.js:584
    throw err;
    ^

Error: Cannot find module 'nice-try'
    at Function.Module._resolveFilename (internal/modules/cjs/loader.js:582:15)
    at Function.Module._load (internal/modules/cjs/loader.js:508:25)
    at Module.require (internal/modules/cjs/loader.js:637:17)
    at require (internal/modules/cjs/helpers.js:22:18)
    at Object.<anonymous> (/Users/noot/projects/web/self-order/node_modules/cross-spawn/lib/parse.js:4:17)
    at Module._compile (internal/modules/cjs/loader.js:701:30)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:712:10)
    at Module.load (internal/modules/cjs/loader.js:600:32)
    at tryModuleLoad (internal/modules/cjs/loader.js:539:12)
    at Function.Module._load (internal/modules/cjs/loader.js:531:3)
error Command failed with exit code 1.
```

To solve this issue, you just run

```script
rm -rf node_modules
npm install
```

## Reference

[https://stackoverflow.com/a/30436256](https://stackoverflow.com/a/30436256)

