FROM debian:12.6-slim

RUN apt update \
    && apt install -y curl git nginx

RUN mkdir -p /etc/nginx
COPY ./etc/nginx/nginx.conf /etc/nginx/nginx.conf

CMD ["nginx", "-c", "/etc/nginx/nginx.conf", "-g", "daemon off;"]
