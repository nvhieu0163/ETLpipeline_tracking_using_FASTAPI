from flask import Flask

from dir_import_app.define_job_import import LIST_JOB

import_app = Flask(
    import_name='[LOCAL_CLUSTER] FlaskAPI app to call import data'
)

@import_app.route("/")
def root():
    return {"message" : "Hello there!"}, 200


@import_app.route("/get-help")
def get_help():
    return {"message": "This is a help string"}, 200


@import_app.route("/job/import")
def import_data(job_name : str):
    if job_name in LIST_JOB.keys():
        LIST_JOB[job_name]()
        return {"message" : f"import '{job_name}' successfully", "status" : 200}
    else:
        return f"no job name '{job_name}' available", 404


if __name__ == '__main__':
    import_app.run(debug=True, port=8689)