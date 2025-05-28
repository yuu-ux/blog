#!/bin/bash

/root/.rye/shims/rye run python /root/admin/seeder/imports/import_member.py
/root/.rye/shims/rye run python /root/admin/seeder/imports/import_category.py
/root/.rye/shims/rye run python /root/admin/seeder/imports/import_post.py
