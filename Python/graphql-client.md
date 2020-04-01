# GraphQL client

```python
import requests

url = 'https://api.github.com/graphql'
json = { 'query' : '{ viewer { repositories(first: 30) { totalCount pageInfo { hasNextPage endCursor } edges { node { name } } } } }' }
api_token = "your api token here..."
headers = {'Authorization': 'token %s' % api_token}

r = requests.post(url=url, json=json, headers=headers)
print (r.text)
```

[https://stackoverflow.com/a/46271487](https://stackoverflow.com/a/46271487)