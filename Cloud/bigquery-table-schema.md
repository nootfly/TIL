# Show biquery table schema

```sh
bq show project:sales.transactions

bq show --schema --format=prettyjson sales.transactions >  ./myschema.json
```

[https://stackoverflow.com/a/50921844](https://stackoverflow.com/a/50921844)

[https://cloud.google.com/bigquery/docs/schemas](https://cloud.google.com/bigquery/docs/schemas)
