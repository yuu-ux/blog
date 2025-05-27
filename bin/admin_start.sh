#!/bin/bash
npx tailwindcss -i /home/blog/admin/static/style.css -o /home/blog/admin/static/dist.css

# Flaskサーバー起動（gunicorn または flask run）
exec gunicorn --bind 0.0.0.0:9001 admin:app --log-level --pid /run/gunicorn-admin.pid
