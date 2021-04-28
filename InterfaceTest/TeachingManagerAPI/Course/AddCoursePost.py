import requests

host = 'http://127.0.0.1:80'
api_url = f'{host}/api/mgr/sq_mgr/'

header = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
params = {
    'action': 'add_course',
    'data': """{
        "name": "测试课程",
        "desc": "This is a test!!!",
        "display_idx" : "5"
    }"""
}

resp = requests.post(api_url, data=params)
resp.encoding = 'unicode_escape'

print(resp.request.headers['Content-Type'])
print(resp.request.body)
print(resp.text)










