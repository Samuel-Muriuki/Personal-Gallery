#!/bin/bash

# Build the project
echo "Building the project..."
sudo apt-get install libpq-dev
pip install psycopg2-binarypip install psycopg2pip install wheel setuptools pip --upgrade
pip3 install wheel

python -m pip install wheel setuptools pip --upgrade
python3 -m pip install wheel setuptools pip --upgrade
py -m pip install wheel setuptools pip --upgrade
pip install wheel setuptools pip --upgrade
pip3 install wheel setuptools pip --upgrade

python3 -m pip install -r requirements.txt

echo "Make Migration..."
python3 manage.py makemigrations
python3 manage.py migrate

echo "Collect Static..."
python3 manage.py