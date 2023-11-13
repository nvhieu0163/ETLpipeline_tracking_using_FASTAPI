import json

import requests

# curl -d '{"title":"my title", "message":"my message", "uidUsername":"my name", "guidGroupNameAlias":"DWH_JOB_NOTI"}' -X POST -H 'token: 0735fd9182d039594c4fa435505986db7d15BHea' -H 'Content-Type: application/json' --insecure http://10.210.12.92:8688/dataApi/dLinkNoti/group 

##########################################################################################
# TEST using FastAPI
##########################################################################################

# url = 'http://127.0.0.1:8688/job/import?job_name=Northwind_orders_SyncJob'
# response = requests.get(url=url)
# print(response.text)
# print(response.status_code)


#############
# params = {
#   "title": "Đây là title",
#   "message": "Đây là message",
#   "uidUsername": "hieu.nguyenvu",
#   "guidChannelName": "group_name"
# }

# headers = {
#     'token' : 'ZKRrWBKgRrOJ5hNF7ti1t4tqGfipSuhXbA6VGtlH',
#     'Content-Type' : 'application/json'
# }

# CHANNEL_URL = 'http://127.0.0.1:8689/noti/dlink'
# res = requests.get("http://127.0.0.1:8689/get-token")
# res = requests.post(CHANNEL_URL, headers=headers, json=params)

# if res.status_code != 200:
#     print('Noti to REPORT_API failed. Will try again')
#     exit(1)

# print(res.text)


##########################################################################################
# TEST using Flask
##########################################################################################

# url = 'http://127.0.0.1:8688/job/import?job_name=Northwind_orders_SyncJob'
# url = 'http://127.0.0.1:8688/get-token'
# response = requests.get(url=url)
# print(response.text)
# print(response.status_code)


#############
params = {
  "title": "Đây là title",
  "message": "Đây là message",
  "uidUsername": "hieu.nguyenvu",
  "guidGroupNameAlias": "group_name"
}

headers = {
    'token' : 'ZKRrWBKgRrOJ5hNF7ti1t4tqGfipSuhXbA6VGtlH',
    'Content-Type' : 'application/json'
}

CHANNEL_URL = 'http://127.0.0.1:8689/noti/telegram'

res = requests.get("http://127.0.0.1:8689/get-token")
print(res.text)
res = requests.post(CHANNEL_URL, headers=headers, json=params)
print(res.text)

if res.status_code != 200:
    print('Noti to REPORT_API failed. Will try again')
    exit(1)
