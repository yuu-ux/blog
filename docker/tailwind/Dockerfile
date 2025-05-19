FROM debian:12.5

RUN apt update && apt install -y curl gnupg \
  && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
  && apt install -y nodejs

COPY ./admin/package.json ./admin/package-lock.json* /root/admin/

WORKDIR /root/admin

RUN npm install -D tailwindcss autoprefixer postcss @tailwindcss/typography

RUN node_modules/.bin/tailwindcss init
RUN [ -f postcss.config.js ] || echo "module.exports = { plugins: { tailwindcss: {}, autoprefixer: {} } };" > postcss.config.js

COPY ./admin /root
