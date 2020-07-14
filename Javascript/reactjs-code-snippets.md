# React js code sippets

## Sort and Map

```javascript
const myData = [].concat(this.state.data)
    .sort((a, b) => a.itemM > b.itemM ? 1 : -1)
    .map((item, i) => 
        <div key={i}> {item.matchID} {item.timeM}{item.description}</div>
    );
```

