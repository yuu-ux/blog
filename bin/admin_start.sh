#!/bin/bash
npx tailwindcss -i /home/blog/admin/static/style.css -o /home/blog/admin/static/dist.css

exec /home/admin/.rye/shims/rye run gunicorn --bind 0.0.0.0:9001 admin:app
