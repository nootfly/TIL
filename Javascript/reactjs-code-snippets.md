# React js code sippets

## Sort and Map

```javascript
const myData = [].concat(this.state.data)
    .sort((a, b) => a.itemM > b.itemM ? 1 : -1)
    .map((item, i) => 
        <div key={i}> {item.matchID} {item.timeM}{item.description}</div>
    );
```

## scroll to top

```javascript
import React, { useRef } from 'react'

const scrollToRef = (ref) => {
  if (ref) {
    ref.current.scrollIntoView({block: 'start' });
  }

};

const ScrollDemo = () => {

   const myRef = useRef(null)
   const executeScroll = () => scrollToRef(myRef)

   return (
      <> 
         <div ref={myRef}>I wanna be seen</div> 
         <button onClick={executeScroll}> Click to scroll </button> 
      </>
   )
}
```

[https://stackoverflow.com/a/52528619](https://stackoverflow.com/a/52528619)

## Use react-image-crop

[https://github.com/DominicTobias/react-image-crop](https://github.com/DominicTobias/react-image-crop)
[https://levelup.gitconnected.com/crop-images-on-upload-in-your-react-app-with-react-image-crop-5f3cd0ad2b35](https://levelup.gitconnected.com/crop-images-on-upload-in-your-react-app-with-react-image-crop-5f3cd0ad2b35)

## Merging Images Using Javascript/React

[https://github.com/lukechilds/merge-images](https://github.com/lukechilds/merge-images)

```javascript
mergeImages([
  'http://example.com/images/Avatar.png',
  'http://example.com/images/Hat.png',
])
.then((b64) => {
  document.querySelector('img.abc').src = b64;
})
.catch(error => console.log(error))
return (
  ...
      <img class="abc" src='' width={100} height={200} alt="avatar"/>
  ...
);
```

[https://www.npmjs.com/package/merge-images](https://www.npmjs.com/package/merge-images)
