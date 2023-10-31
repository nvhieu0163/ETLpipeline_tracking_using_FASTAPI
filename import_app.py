from fastapi import FastAPI, HTTPException

from dir_import_app.define_job_import import LIST_JOB

import_app = FastAPI(
    title = "[LOCAL_CLUSTER] FastAPI app to call import data",
    description = "A demo FastAPI project for: calling import data tasks after ETL pipeline finished in Airflow",
    docs_url= "/docs",
    redoc_url= "/redoc"
)

@import_app.get("/")
def root():
    return {"message" : "Hello there!"}


@import_app.get("/get-help")
def get_help():
    return {"message": "This is a help string", "status": 200}


@import_app.get("/job/import")
def import_data(job_name : str):
    if job_name in LIST_JOB.keys():
        LIST_JOB[job_name]()
        return {"message" : f"import '{job_name}' successfully", "status" : 200}
    else:
        raise HTTPException(status_code=404, detail=f"no job name '{job_name}' available")