import requests


class Login:
    def __init__(self):
        self.url = 'http://localhost:/api/mgr/loginReq'

    def login(self, username, password):
        data = {
            'username': username,
            'password': password
        }
        rep = requests.post(self.url, data=data)
        print(rep.json())
        print(rep.cookies['sessionid'])
        return rep.cookies['sessionid']


if __name__ == '__main__':
    Login().login('auto', 'sdfsdfsdf')

