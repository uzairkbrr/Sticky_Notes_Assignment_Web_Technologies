#!/bin/bash

# Exit script out completely if any command fails
set -e

echo "====================================="
echo "  Starting Ideaflip Notes Project"
echo "====================================="

# Check if pip is installed
if ! command -v pip &> /dev/null
then
    echo "pip could not be found. Please install Python and pip first."
    exit 1
fi

echo "Installing Django..."
pip install django

echo "Applying Database Migrations..."
python manage.py makemigrations notes
python manage.py migrate

echo "Starting Django Development Server on port 8000..."
python manage.py runserver 0.0.0.0:8000
