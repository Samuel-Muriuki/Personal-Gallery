#!/bin/bash

# Build the project
echo "Building the project..."
sudo apt-get install libpq-dev

python3 -m pip install -r requirements.txt

echo "Make Migration..."
python3 manage.py makemigrations
python3 manage.py migrate

echo "Collect Static..."
python3 manage.py