many1#Go
ssh sen@144.126.218.243

<!-- todo -->
- _react table break down_
- _table render_
- associate pedidos entity
- sync function
    - clientes, vendedores
    -  


# Setup
[Digital Ocean ]( https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04#create-and-configure-a-new-django-project)


### Security
[Server security](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-16-04)
SSH keys and group acess

### Complete Digital Ocean Django React setup
[MVP Deployment](https://medium.com/geekculture/deploy-a-mvp-django-react-web-application-to-digital-ocean-1a35a4359a5b)

[Nginx config](https://stackoverflow.com/questions/65124421/deploy-both-django-and-react-on-cloud-using-nginx)
[Another config]
```

# Disable emitting nginx version in the "Server" response header field
server_tokens             off;

# Use site-specific access and error logs
access_log                /var/log/nginx/sudan_art.access.log;
error_log                 /var/log/nginx/sudan_art.error.log;


server {
    listen       80;
    listen [::]:80;
    server_name  sudan-art.com www.sudan-art.com;
    client_max_body_size 15M;

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 default_server ssl http2;
    listen [::]:443 ssl http2;
    client_max_body_size 15M;

    server_name  sudan-art.com www.sudan-art.com;

    ssl_certificate /etc/nginx/ssl/live/sudan-art.com/fullchain.pem;
    ssl_certificate_key /etc/nginx/ssl/live/sudan-art.com/privkey.pem;

    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
        try_files $uri /index.html;
    }

    location /api/artwork {
        try_files $uri$is_args$query_string @proxy_api;
    }

    location /recent {
        try_files $uri @proxy_api;
    }

    location /upload {
        try_files $uri @proxy_api;
    }

    location @proxy_api {
    # Django refers to docker service name
    proxy_pass            http://django:8000;
    proxy_set_header      Host $host;
    proxy_set_header      X-Forwarded-Proto $scheme;
    proxy_set_header      X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_redirect        off;
  }
}
```