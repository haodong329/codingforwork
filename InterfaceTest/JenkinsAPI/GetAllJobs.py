import unittest
import requests

class GetAllJobs(unittest.TestCase):
    def setUp(self):
        self.url='http://localhost:8080/api/json?tree=jobs[name]'
        self.ExpectName = ['AutomationTest', 'Get_PythonInfo']

    def testGetAllJobs(self):
        response=requests.get(self.url,auth=('admin','admin'))
        codeResult=response.status_code
        jsonResult=response.json()
        #判断响应状态码
        self.assertEqual(codeResult,200)

        #取出所有Job名称，判断Job名字是否正确完整
        job = jsonResult['jobs']
        endList = []
        if codeResult == 200:
            for i in job:
                endList.append(i['name'])
        self.assertEqual(endList,self.ExpectName)


    def tearDown(self):
        print("已经完成了本次接口测试!!!")

if __name__=="__mian__":
    unittest.main()