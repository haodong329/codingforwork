import unittest
import requests

# java -jar moco-runner-0.10.0-standalone.jar  http -p 12306 -c config.json
class TestMoco1(unittest.TestCase):
    def setUp(self):
        self.url='http://localhost:12306/moco1'

    def testGetAllJobs(self):
        response=requests.get(self.url)
        code=response.status_code
        self.assertEqual(code,200)

    def tearDown(self):
        print("已经完成了本次接口测试!!!")

if __name__=="__mian__":
    unittest.main()