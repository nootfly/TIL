# Material UI code snippets

## Set Typography Text Color in Material UI

```javascript
import React from "react";
import { withStyles } from "@material-ui/core/styles";
import Typography from "@material-ui/core/Typography";

const WhiteTextTypography = withStyles({
  root: {
    color: "#FFFFFF"
  }
})(Typography);

export default function App() {
  return (
    <div className="App" style={{ backgroundColor: "black" }}>
      <WhiteTextTypography variant="h3">
        This text should be white
      </WhiteTextTypography>
    </div>
  );
}
```

[https://stackoverflow.com/a/60609045](https://stackoverflow.com/a/60609045)
