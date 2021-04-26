class SmallFunctionCode:
    #实现对字符串的反转
    def reversal(self):
        str = '123456789'
        a = list()
        for i in range(0, len(str)):
            a.append(str[i:i + 1])
        #利用列表可以自带反转的方法
        a.reverse()

        end = ''
        for j in range(0, len(a)):
            end = end + a[j]
        print("原数据：")
        print(str+'\n') #换行
        print("反转后数据：")
        print(end)


    def test1(self):
        dic = {
            "age": '11',
            "name": "haodong"
        }
        for i in dic:
            print(i)
        for j,h in dic.items():
            print(j)
            print(h)


if __name__=="__main__":
    s=SmallFunctionCode()
    s.test1()