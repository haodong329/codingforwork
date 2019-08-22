import unittest
import requests

class DisablePythonInfo(unittest.TestCase):
    def setUp(self):
        self.url='http://localhost:8080/job/PythonInfo/disable'

    def testGetAllJobs(self):
        response=requests.post(self.url,auth=('admin','admin'))
        code=response.status_code
        self.assertEqual(code,200)

    def tearDown(self):
        print("已经完成了本次接口测试!!!")

if __name__=="__mian__":
    unittest.main()