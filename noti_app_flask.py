from flask import Flask, Response, request

from dir_noti_app.authenticator import Authenticator
from dir_noti_app.notify_dlink import notify_dlink
from dir_noti_app.notify_telegram import notify_telegram

###########################################
noti_app = Flask(
    import_name = "FlaskAPI to notify"
    # static_host = '127.0.0.1'
    # title = "[LOCAL_CLUSTER] Flask app to notify Job Status",
    # description = "A demo Flask project for: notifying job status of ETL pipeline in Airflow"
)
au = Authenticator(seed=20)

@noti_app.route("/") # mặc định là GET 
def root():
    return {"message" : "Hello there!"}


@noti_app.route("/get-help")
def get_help():
    return {"message": "This is a help string"}


@noti_app.route('/get-token', methods=['GET', 'POST'])
def get_token():
    # print(request.remote_addr)    127.0.0.1
    # print(request.host_url)       http://127.0.0.1:8688/
    if au.authenticate_host(request.remote_addr):
        token = au.get_token()
        if not token:
            return {"message": "No token available, contacts administrator for more tokens"}
        return {"message": "Get token sucessfully", "new_token" : f"{token}"}
    else:
        return "Your host is not accepted!", 401
    

@noti_app.route('/delete_active_tokens', methods = ['POST'])
def delete_all_tokens():
    if request.remote_addr == '127.0.0.1':
        au.delete_all_active_tokens()
        return {"message": "Deletes all tokens sucessfully"}
    else:
        return "Your host is not accepted to do this action!", 401


#############################################
@noti_app.route("/noti/dlink", methods = ['GET', 'POST', 'PUT'])
def noti_dlink():
    token = request.headers.get('token')
    host = request.remote_addr
    print("Client Token: ", token)
    print("Client Host: ", host)
    if au.authenticate(host=host, TOKEN=token):
        request_data = request.get_json()
        notify_dlink(
            message = request_data['title'] + ": " + request_data['message'] + '\n', 
            user_name = request_data['uidUsername'],
            group_name= request_data['guidGroupNameAlias']
        )
    else:
        return f"Authentication is not success!", 401

    return "notify dlink successful", 200


@noti_app.route("/noti/telegram", methods = ['GET', 'POST', 'PUT'])
def noti_telegram():
    token = request.headers.get('token')
    host = request.remote_addr
    print("Client Token: ", token)
    print("Client Host: ", host)
    if au.authenticate(host=host, TOKEN=token):
        request_data = request.get_json()
        notify_telegram(
            message = request_data['title'] + ": " + request_data['message'] + '\n', 
            user_name = request_data['uidUsername'],
            group_name= request_data['guidGroupNameAlias']
        )
    else:
        return f"Authentication is not success!", 401

    return "notify telegram successful", 200


if __name__ == '__main__':
    noti_app.run(debug=True, port=8689)


# print(request.headers)
# print(request.args)
# print(request.data)
# print(request.base_url)
# print(request.content_md5)