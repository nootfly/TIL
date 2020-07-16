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
