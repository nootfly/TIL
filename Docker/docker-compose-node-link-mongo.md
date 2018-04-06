# docker-compose node link mongo

1. Create a `Dockerfile`

   ```
   FROM node:6.9.4-alpine
   ADD . /usr/src/app
   WORKDIR /usr/src/app
   RUN npm install
   CMD ["npm", "start"]  
   ```
2. Create `docker-compose.yaml`, and pay attention to the service names which should not include `_`.

   ```
   version: '2.1'
   services:
    mongodbservice:
     container_name: mongo
     image: mongo
     ports:
       - "27017:27017"
     volumes:
       - ./db:/data/db
    web:
     container_name: web
     build: .
     depends_on:
        - mongodbservice
     volumes:
        - ./:/usr/src/app
     links:
       - mongodbservice
     ports:
       - "3000:3000"
   ```
3. In code, use the correct mongodb URL

   `let mongodb = mongojs('mongodb://mongodbservice:27017/Test', ['test']);`
