# coding = utf-8
# 冒泡排序
nums=input().split()
for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        if int(nums[j])>=int(nums[i]):
            tep=nums[i]
            nums[i]=nums[j]
            nums[j]=tep
print(nums)