#!/bin/bash

rm -f db.sqlite3
rm -f engine/migrations/0*.py
./manage.py makemigrations
./manage.py migrate

