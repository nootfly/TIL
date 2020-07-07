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

## material UI add background images

```javascript
import React from 'react';

import Paper from 'material-ui/Paper';

import IconButton from 'material-ui/IconButton';
import ActionHome from 'material-ui/svg-icons/action/home';

import Image from '../img/main.jpg'; // Import using relative path


const styles = {
    paperContainer: {
        backgroundImage: `url(${Image})`
    }
};

export default class Home extends React.Component{
    render(){
        return(
            <Paper style={styles.paperContainer}>
                Some text to fill the Paper Component
            </Paper>
        )
    }
}
```

[https://stackoverflow.com/a/47145247](https://stackoverflow.com/a/47145247)
