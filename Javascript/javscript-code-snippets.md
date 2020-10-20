# Javascript code snippets

## array filter

```javascript
const filteredHomes = json.homes.filter(x => x.price <= 1000 && x.sqft >= 500 && x.num_of_beds >=2 && x.num_of_baths >= 2.5);
```

## substring

```javascript
var id = "ctl03_Tabs1";
var lastFive = id.substr(id.length - 5); // => "Tabs1"
var lastChar = id.substr(id.length - 1);
```

## loop dictionary

```javascript
for (const [key, value] of Object.entries(object)) {
  console.log(key, value);
}
```

## Checking if a key exists in a JavaScript object

```javascript
("key" in obj)
```

## `slice`

The slice() method returns the selected elements in an array, as a new array object.

The slice() method selects the elements starting at the given start argument, and ends at, but does not include, the given end argument.

```javascript
var fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
var citrus = fruits.slice(1, 3); // "Orange", "Lemon"
```

[https://www.w3schools.com/jsref/jsref_slice_array.asp](https://www.w3schools.com/jsref/jsref_slice_array.asp)

## Resize the canvas output image

```javascript
var resizedCanvas = document.createElement("canvas");
var resizedContext = resizedCanvas.getContext("2d");

resizedCanvas.height = "100";
resizedCanvas.width = "200";

var canvas = document.getElementById("original-canvas");

resizedContext.drawImage(canvas, 0, 0, 200, 100);
var myResizedData = resizedCanvas.toDataURL();
```

[https://stackoverflow.com/a/23481814](https://stackoverflow.com/a/23481814)

## Base64 PNG data to HTML5 canvas

```javascript
var canvas = document.getElementById("c");
var ctx = canvas.getContext("2d");

var image = new Image();
image.onload = function() {
  ctx.drawImage(image, 0, 0);
};
image.src = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAIAAAACDbGyAAAAAXNSR0IArs4c6QAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9oMCRUiMrIBQVkAAAAZdEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAAADElEQVQI12NgoC4AAABQAAEiE+h1AAAAAElFTkSuQmCC";
```

```html
<canvas id="c"></canvas>
```

[https://stackoverflow.com/a/4409745](https://stackoverflow.com/a/4409745)

## Add images to canvas

```javascript
var canvas = document.getElementById('viewport'),
context = canvas.getContext('2d');

make_base();

function make_base()
{
  base_image = new Image();
  base_image.src = 'img/base.png';
  base_image.onload = function(){
    context.drawImage(base_image, 0, 0);
  }
}
```

[https://stackoverflow.com/a/6011402](https://stackoverflow.com/a/6011402)

## Wirte text on top of images in HTML5 canvas

```javascript
window.onload = function(){
     var canvas = document.getElementById("myCanvas");
     var context = canvas.getContext("2d");
     var imageObj = new Image();
     imageObj.onload = function(){
         context.drawImage(imageObj, 10, 10);
         context.font = "40pt Calibri";
         context.fillText("My TEXT!", 20, 20);
     };
     imageObj.src = "darth-vader.jpg"; 
};

```

[https://stackoverflow.com/a/8429496](https://stackoverflow.com/a/8429496)
