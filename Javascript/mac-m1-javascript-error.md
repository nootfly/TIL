# Mac m1 javascript error

## error:0308010C:digital envelope routines::unsupported

```sh
export NODE_OPTIONS=--openssl-legacy-provider
```

[https://stackoverflow.com/a/69699772](https://stackoverflow.com/a/69699772)

## Error: Node Sass does not yet support your current environment: OS X Unsupported architecture (arm64) with Unsupported runtime

```sh
rm -rf node_modules
npm install --target_arch=x64
```

[https://stackoverflow.com/a/68111769](https://stackoverflow.com/a/68111769)
