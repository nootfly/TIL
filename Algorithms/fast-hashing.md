# Open addressing hash tables

> This is not an advanced topic at all, but it is worth emphasizing: for small keys, open addressing hash tables are consistently faster and smaller than a standard chaining based hash tables. C++11 requires std::unordered_map to use chaining, which means if you want an efficient hash table for lots of small keys, choose another library.

## Reference

[Advanced techniques to implement fast hash tables](https://attractivechaos.wordpress.com/2018/10/01/advanced-techniques-to-implement-fast-hash-tables/)