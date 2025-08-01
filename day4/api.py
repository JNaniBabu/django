import requests,json

u="http://127.0.0.1:8000/post/"
data={"name":"jakkula"}
data=json.dumps(data)
requests.post(url=u,data=data)




