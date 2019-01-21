# Config environment variables in Vuejs

```json
//.eslintrc.js
module.exports = {
    
        "root": true,
        "env": {
          "node": true
        },
        "extends": [
          "plugin:vue/essential",
          "eslint:recommended"
        ],
        "rules": {
        'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
          'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
        },
        "parserOptions": {
          "parser": "babel-eslint"
        }
      
}
```

```config
//in .env.development
VUE_APP_WORK_TIME=0.1

//in js
WorkTime: process.env.VUE_APP_WORK_TIME
```