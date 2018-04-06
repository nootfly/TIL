# Semver for consumers

As a consumer, you can specify which kinds of updates your app can accept in the package.json file.

If you were starting with a package 1.0.4, this is how you would specify the ranges:

Patch releases: 1.0 or 1.0.x or ~1.0.4
Minor releases: 1 or 1.x or ^1.0.4
Major releases: * or x

Reference: [https://docs.npmjs.com/getting-started/semantic-versioning](https://docs.npmjs.com/getting-started/semantic-versioning)