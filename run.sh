#!/bin/bash

# Run the first Python script
python pre_requisites.py

# Start the Cloud Run task
#gunicorn -b 0.0.0.0:8080 -timeout 120 app:app 
python app.py
