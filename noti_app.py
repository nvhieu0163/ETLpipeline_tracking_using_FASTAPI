from typing import Union

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

from dir_noti_app.authenticator import Authenticator
from dir_noti_app.notify_dlink import notify_dlink
from dir_noti_app.notify_telegram import notify_telegram

###########################################
noti_app = FastAPI(
    title = "[LOCAL_CLUSTER] FastAPI app to notify Job Status",
    description = "A demo FastAPI project for: notifying job status of ETL pipeline in Airflow",
    docs_url= "/docs",
    redoc_url= "/redoc"
)
au = Authenticator(seed=20)

@noti_app.get("/")
def root():
    return {"message" : "Hello there!"}


@noti_app.get("/get-help")
def get_help():
    return {"message": "This is a help string"}


@noti_app.get('/get-token')
def get_token(request : Request):
    if au.authenticate_host(request.client.host):
        token = au.get_token()
        if not token:
            return {"message": "No token available, contacts administrator for more tokens"}
        return {"message": "Get token sucessfully", "new_token" : f"{token}"}
    else:
        raise HTTPException(status_code=401, detail=f"Your host is not accepted!")
    

@noti_app.get('/delete_active_tokens')
def delete_all_tokens(request : Request):
    if request.client.host == '127.0.0.1':
        au.delete_all_active_tokens()
        return {"message": "Deletes all tokens sucessfully"}
    else:
        raise HTTPException(status_code=401, detail=f"Your host is not accepted!")


#############################################
class params(BaseModel):
    title : str
    message : str
    uidUsername : Union [str, None] = None
    guidGroupNameAlias : str


@noti_app.post("/noti/dlink")
def noti_dlink(info : params, request : Request):
    token = request.headers.get('token')
    host = request.client.host

    if au.authenticate(host=host, TOKEN=token):
        notify_dlink(
            message = info.title + ": " + info.message + '\n', 
            user_name = info.uidUsername, 
            group_name= info.guidGroupNameAlias
        )
    else:
        raise HTTPException(status_code=401, detail=f"Authentication got error!")

    return info


@noti_app.post("/noti/telegram")
def noti_telegram(info : params, request : Request):
    token = request.headers.get('token')
    host = request.client.host

    if au.authenticate(host=host, TOKEN=token):
        notify_telegram(
            message = info.title + ": " + info.message + '\n', 
            user_name = info.uidUsername, 
            group_name= info.guidGroupNameAlias
        )
    else:
        raise HTTPException(status_code=401, detail=f"Authentication got error!")

    return info


# print(request.headers)
# print(request.client)
# print(type(request.client))
# print(request.app)
# print(request.base_url)
# print(request.cookies)
# print(request.auth)
# print(request.method)
# print(request.user)
# print(request.state)
# print(request.query_params)