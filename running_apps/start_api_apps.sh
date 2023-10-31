#!/bin/bash

cd '/home/airflow/Codes/fastAPI_for_airflow_project'
echo `pwd`
nohup ./fastapi-venv/bin/uvicorn noti_app:noti_app --port 8689 > ./running_apps/log_noti_app.txt &
nohup ./fastapi-venv/bin/uvicorn import_app:import_app --port 8688 > ./running_apps/log_import_app.txt &
