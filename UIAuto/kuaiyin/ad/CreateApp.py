from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 指定deriver路径
service=Service('/usr/local/bin/chromedriver')
driver=webdriver.Chrome(service=service)

# 设置元素隐形等待时间
driver.implicitly_wait(20)


# driver.maximize_window()# 浏览器最大化
# 进行登陆操作
driver.find_element(By.XPATH,'//*[@id="input-18"]').send_keys('18582897286')
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('tDpBzzzZ7p')
driver.find_element(By.XPATH,'//*[@id="app-container"]/div/div/div[2]/div/div[2]/button/span').click()
# 进入APP 产品管理
driver.find_element(By.XPATH,'//*[@id="app"]/section/aside/ul/li[3]').click()

# 查找所有分页中的appid
appid_list=[]
# 先把第一页的appid添加进去
apps = driver.find_elements(By.XPATH, "//*[@class='el-table_1_column_1 is-center  el-table__cell']")
for i in apps:
    appid_list.append(i.text)
# 如果有分页数据，把分页的appid进行添加
while 1:
    if driver.find_element(By.XPATH,'''//*[@class="btn-next"]''').is_enabled():
        driver.find_element(By.XPATH, '//*[@class="btn-next"]').click()
        time.sleep(1) #需要添加一个等待时间，翻页有一个加载时间
        apps = driver.find_elements(By.XPATH, "//*[@class='el-table_1_column_1 is-center  el-table__cell']")
        if apps:
            for i in apps:
                appid_list.append(i.text)
        else:
            print('没有元素了添加什么！！！')
    else:
        print('没有下一页，不需要进行翻页操作，已完成appid的查找！')
        break

# 初始化自动化的appid命名，防止与已经存在的appid重复
app_id=80001
while 1:
    if app_id in [int(i) for i in appid_list]:
        app_id = app_id + 1
    else:
        break
# 创建app
driver.find_element(By.XPATH,'//*[@class="el-form-item__content"]/button').click()
driver.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div[2]/div/div/div[2]/form/div[1]/div/div/input').send_keys('UI自动化测试建立')
driver.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div[2]/div/div/div[2]/form/div[2]/div/div/input').send_keys(app_id)
driver.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div[2]/div/div/div[2]/form/div[3]/div/div/div/div/input').click()
driver.find_element(By.XPATH,"//div[@data-popper-placement='bottom-start']/div/div/div/ul/li[2]").click()
driver.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div[2]/div/div/div[2]/form/div[4]/div/div[1]/input').send_keys('com.test.cn')
driver.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div[2]/div/div/div[3]/div/button[2]/span').click()

# time.sleep(30)

# # 定位元素
# def find_element(timeout=20,poll_frequency=0.5,**kwargs):
#     try:
#         return WebDriverWait(driver,timeout=timeout,poll_frequency=poll_frequency)\
#         .until(EC.presence_of_element_located(By.XPATH),kwargs.get('path'))
#     except TimeoutException as e:
#         logging.info('定位元素失败 %s' %e)
#         raise Exception('元素定位失败,请检查元素路径！！！')

def find_element2(self, timeout=10, poll_frequency=0.5, **kwargs):
    """
    元素定位操作
    :param locator: 定位器
    :param timeout:  超长时间
    :param poll_frequency:  间隔时间
    :return:  返回webwlement对象
    """
    try:
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
            EC.element_to_be_clickable((By.XPATH, kwargs.get("xpath"))), message="元素定位失败")
    except TimeoutException as e:
        self.logger.info("元素定位失败：%s" % e)
        raise Exception('元素定位失败，请检查xpath数据是否正确')