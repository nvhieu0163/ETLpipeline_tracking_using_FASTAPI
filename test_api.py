import json

import requests

url = 'http://127.0.0.1:8000/job/import?job_name=Northwind_orders_SyncJob'

response = requests.get(url=url)
print(response.text)



#############################################
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

# CHANNEL_URL = 'http://127.0.0.1:8000/noti/dlink'

# res = requests.post(CHANNEL_URL, headers=headers, json=params)

# if res.status_code != 200:
#     print('Noti to REPORT_API failed. Will try again')
#     exit(1)

# print(res.text)
