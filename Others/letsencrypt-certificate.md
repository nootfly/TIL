# letsencrypt certificate

1. Use this docker command generate a SSL certificate, you can choose option 2 after you run this command.

   ```shell
   docker run -it --rm -p 443:443 -p 80:80 --name certbot \
      -v "/etc/letsencrypt:/etc/letsencrypt" \
      -v "/var/lib/letsencrypt:/var/lib/letsencrypt" \
      quay.io/letsencrypt/letsencrypt:latest auth --server https://acme-v01.api.letsencrypt.org/directory \
      --debug --renew-by-default --standalone-supported-challenges http-01 \
      --verbose -d yourdomain  --text --agree-tos --email youremail@gmail.com
   ```

2. Config nginx


  ```
      server {
        listen 80;
        server_name  yourdomain;

        return 301 https://$host$request_uri;
       }

      server {
        listen       443 ssl;
        server_name  yourdomain;

        ssl_certificate /etc/letsencrypt/live/yourdomain/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/yourdomain/privkey.pem;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_prefer_server_ciphers on;
        ssl_ciphers "HIGH:!aNULL:!MD5 or HIGH:!aNULL:!MD5:!3DES";


        location / {
            proxy_pass   http://site2/;
            proxy_redirect     off;
                proxy_set_header   Host $host;
                proxy_set_header   X-Real-IP $remote_addr;
                proxy_set_header   X-Forwarded-For     $proxy_add_x_forwarded_for;
                proxy_set_header   X-Forwarded-Host $server_name;
        }
      }
      upstream site2 {
       server site2:8081;
      }
   ```
