# ReactJs development problem solutions

## Remove `react-router-dom` `Link` underscore

```javascript
<Link to={'/accounts'} style={{ color: 'inherit', textDecoration: 'inherit'}}>
```

[https://stackoverflow.com/a/56158634](https://stackoverflow.com/a/56158634)

## set textfiled value

```javascript
<input type="text" placeholder="First Name" onChange={e => setfName(e.target.value)} />
```

[https://stackoverflow.com/a/57343140](https://stackoverflow.com/a/57343140)

## axios instance set header

```javascript
Object.assign(instance.defaults, {headers: {authorization: 'foo bar'}});
//or
instance.defaults.headers.common['Authorization'] = authToken;
```

[https://github.com/axios/axios/issues/209](https://github.com/axios/axios/issues/209)

## Cannot read property of undefined in Reactjs

```javascript
{this.state.list && <MyMeetingList meetings={this.state.list} />}
```

[https://stackoverflow.com/a/47744911](https://stackoverflow.com/a/47744911)

## Note: the react docs suggest that user-defined components must be capitalized before their use in JSX to avoid being treated as HTML elements.
