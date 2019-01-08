# ReactJS: Maximum update depth exceeded error

Cause: hat because you calling toggle inside the render method which will cause to re-render and toggle will call again and re-rendering again and so on

Change

```javascript
{<td><span onClick={this.toggle()}>Details</span></td>}
```

To

```javascript
{<td><span onClick={this.toggle}>Details</span></td>}
```

## Reference

[https://stackoverflow.com/a/48497410](https://stackoverflow.com/a/48497410)
