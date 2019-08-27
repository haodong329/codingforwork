import requests
import unittest

class CorrentUserPassw(unittest.TestCase):
    def setUp(self):
        self.url='http://localhost:/api/mgr/loginReq'
        self.username='auto'
        self.password='sdfsdfsdf'

    def testCorrentUP(self):
        data={
            'username':self.username,
            'password':self.password
        }
        #不需要请求头也行
        headers={
            'Host':'restapi-teach.com',
            'Content-Type':'application/x-www-form-urlencoded'
        }
        response=requests.post(self.url,data=data,headers=headers)
        resValue=response.json()
        resHeaders=response.headers

        #1.判断状态码
        self.assertEqual(response.status_code,200)
        #2.断言响应数据
        self.assertEqual(resValue['retcode'],0)
        #3.断言响应数据类型
        for key in resHeaders:
            if key=='Content-Type':
                self.assertEqual(resHeaders[key],"application/json")
            # print(key+":"+resHeaders[key])


        # print(response.cookies)


    def tearDown(self):
        print("本次接口测试结束！！！")

if __name__=="__mian__":
    unittest.main()
