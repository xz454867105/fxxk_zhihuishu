import os,time,json
from selenium.webdriver.chrome.options import Options
import socket
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from itertools import combinations, permutations

# class DebugBrowser:
#     def __init__(self):
#         self.ip = '127.0.0.1'
#         self.port = 9222
#         self.userfile = 'saves/testfile'
#         self.option = Options()
#
#     def debug_chrome(self):
#         # self.options.add_argument('blink-settings=imagesEnabled=true')  # 不加载图片, 提升速度，但无法显示二维码
#         # self.options.add_argument('--headless')
#         # self.options.add_argument('--disable-extensions')
#         # self.options.add_argument('--disable-gpu')
#         # self.options.add_argument('--no-sandbox')
#         self.option.add_argument('--mute-audio')  # 关闭声音
#         self.option.add_argument('--window-size=1024,768')
#         self.option.add_argument('--log-level=3')
#         if self.check_port():
#             self.option.add_experimental_option('debuggerAddress', '{}:{}'.format(self.ip, self.port))
#         else:
#             os.popen('cd C:/Program Files/Google/Chrome/Application'
#     ' && chrome.exe --remote-debugging-port={} --user-data-dir="{}"'.format(self.port, self.userfile))
#             self.option.add_experimental_option('debuggerAddress', '{}:{}'.format(self.ip,  self.port))
#         return self.option
#
#     def check_port(self):
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         result = sock.connect_ex((self.ip, self.port))
#         if result == 0:
#             check = True
#         else:
#             check = False
#         sock.close()
#         return check


class title_of_login:
    def __call__(self, driver):
        """ 用来结合webDriverWait判断出现的title """
        is_title2 = bool(EC.title_is(u'智慧树在线教育_全球大型的学分课程运营服务平台')(driver))
        if is_title2:
            return True
        else:
            return False


class Login:
    def __init__(self):
        self.option = Options()
        self.option.add_argument('blink-settings=imagesEnabled=true')  # 不加载图片, 提升速度，但无法显示二维码
        if int(input('请初始化设置\n1.无界面\n0.有界面\n请输入数字(1/0):')) == 1:
            self.option.add_argument('--headless')
            self.option.add_argument('--disable-extensions')
            self.option.add_argument('--disable-gpu')
            self.option.add_argument('--no-sandbox')

        self.option.add_argument('--mute-audio')  # 关闭声音
        self.option.add_argument('--window-size=1024,768')
        self.option.add_argument('--log-level=3')
        # self.debug = DebugBrowser()
        # self.driver = webdriver.Chrome(options=self.debug.debug_chrome())
        self.driver = webdriver.Chrome(chrome_options=self.option)

    def showQRcode(self):
        i = 0
        us = input('请输入您的账号')
        pa = input('请输入您的密码')


        print("正在打开登陆界面,请稍后")


        self.driver.get('https://passport.zhihuishu.com/login')
        WebDriverWait(self.driver, 30, 0.2).until(
                    lambda driver: driver.find_element_by_class_name("wall-sub-btn"))
        usernm = self.driver.find_element_by_id('lUsername')
        usernm.clear()
        usernm.send_keys(us)
        passwd = self.driver.find_element_by_id('lPassword')
        passwd.clear()
        passwd.send_keys(pa)
        btn = self.driver.find_element_by_class_name('wall-sub-btn')
        btn.click()
        WebDriverWait(self.driver, 270).until(title_of_login())
        time.sleep(5)
        self.driver.get('https://onlineh5.zhihuishu.com/onlineWeb.html#/studentIndex')
        WebDriverWait(self.driver, 30, 0.2).until(lambda driver: driver.find_element_by_class_name("courseName"))
        self.findCourse()
        # self.driver.get(
        #     "https://passport.zhihuishu.com/login?service=https://onlineservice.zhihuishu.com/login/gologin#qrCodeLogin")
        # try:
        #     remover = WebDriverWait(self.driver, 30, 0.2).until(
        #         lambda driver: driver.find_element_by_class_name("switch-nav-wrap"))
        # except exceptions.TimeoutException:
        #     print("网络缓慢，请重试")
        # else:
        #     self.driver.execute_script('arguments[0].remove()', remover)
        #
        # try:
        #     remover = WebDriverWait(self.driver, 30, 0.2).until(
        #         lambda driver: driver.find_element_by_class_name("registerlogo-div"))
        # except exceptions.TimeoutException:
        #     print("当前网络缓慢...")
        # else:
        #     self.driver.execute_script('arguments[0].remove()', remover)
        #
        # try:
        #     remover = WebDriverWait(self.driver, 30, 0.2).until(
        #         lambda driver: driver.find_element_by_class_name("p1"))
        # except exceptions.TimeoutException:
        #     print("当前网络缓慢...")
        # else:
        #     self.driver.execute_script('arguments[0].remove()', remover)
        #
        # try:
        #     remover = WebDriverWait(self.driver, 30, 0.2).until(
        #         lambda driver: driver.find_element_by_class_name("p2"))
        # except exceptions.TimeoutException:
        #     print("当前网络缓慢...")
        # else:
        #     self.driver.execute_script('arguments[0].remove()', remover)
        #
        # try:
        #     remover = WebDriverWait(self.driver, 30, 0.2).until(
        #         lambda driver: driver.find_element_by_class_name("password-icon"))
        # except exceptions.TimeoutException:
        #     print("当前网络缓慢...")
        # else:
        #     self.driver.execute_script('arguments[0].remove()', remover)
        #
        # try:
        #     WebDriverWait(self.driver, 270).until(title_of_login())
        #     cookies = self.driver.get_cookies()
        #     with open('saves/usercookies.json','w') as f:
        #         json.dump(cookies,f)
        #     i = 1
        # except:
        #     print("扫描二维码超时")
        # if i == 1:
            # self.driver.quit()
            # self.findCourse()

    def doMulti(self,quiz,driver):
        choices = driver.find_elements_by_css_selector('svg.topic-option')
        choicesNum = len(choices)
        print('开始尝试所有可能')
        if driver.find_elements_by_css_selector('span.right'):
            print('找到答案')
            driver.find_element_by_css_selector('div.btn').click()
            print('关闭题目')
            time.sleep(0.5)
            try:
                driver.find_elements_by_css_selector('button.el-button--primary')[5].click()
                time.sleep(0.5)
                driver.find_element_by_css_selector('i.iconguanbi').click()
            except:
                pass

        else:
            for i in range(2,choicesNum+1):
                chosen = quiz.find_elements_by_css_selector('svg#iconfuxuanzhong')

                possibles = list(permutations(choices, i))
                for possible in possibles:
                    for p in possible:
                        p.click()
                    time.sleep(1)
                    if driver.find_elements_by_css_selector('span.right'):
                        print('找到答案')
                        driver.find_element_by_css_selector('div.btn').click()
                        print('关闭题目')
                        break
                    else:
                        for p in possible:
                            p.click()

    def doSingle(self,quiz,driver):
        choices = driver.find_elements_by_css_selector('svg.topic-option')
        print('开始尝试所有可能')
        if driver.find_elements_by_css_selector('span.right'):
            print('找到答案')
            driver.find_element_by_css_selector('div.btn').click()
            print('关闭题目')
            time.sleep(0.5)
            try:
                driver.find_elements_by_css_selector('button.el-button--primary')[5].click()
                time.sleep(0.5)
                driver.find_element_by_css_selector('i.iconguanbi').click()
            except:
                pass
        else:
            for choice in choices:
                choice.click()
                time.sleep(1)
                if driver.find_elements_by_css_selector('span.right'):
                    print('找到答案')
                    driver.find_element_by_css_selector('div.btn').click()
                    print('关闭题目')
                    print('继续学习')
                    break


    def doJudge(self,quiz,driver):
        choices = driver.find_elements_by_css_selector('svg.topic-option')
        print('开始尝试所有可能')
        if driver.find_elements_by_css_selector('span.right'):
            print('找到答案')
            driver.find_element_by_css_selector('div.btn').click()
            print('关闭题目')
            time.sleep(0.5)
            try:
                driver.find_elements_by_css_selector('button.el-button--primary')[5].click()
                time.sleep(0.5)
                driver.find_element_by_css_selector('i.iconguanbi').click()
            except:
                pass
        else:
            for choice in choices:
                choice.click()
                time.sleep(1)
                if driver.find_elements_by_css_selector('span.right'):
                    print('找到答案')
                    driver.find_element_by_css_selector('div.btn').click()
                    print('关闭题目')
                    print('继续学习')
                    break

    def watchVideo(self,subchapter,driver):
        first = 1
        time.sleep(5)
        print('看视频')
        time.sleep(1)
        try:
            driver.find_elements_by_css_selector('button.el-button--primary')[5].click()
            time.sleep(0.5)
            driver.find_element_by_css_selector('i.iconguanbi').click()
        except:
            pass



        # while True:
        #     if driver.find_elements_by_css_selector('span.el-dialog__title'):
        #         print('智慧树提示，正在关闭')
        #         warning = driver.find_element_by_css_selector('span.el-dialog__title').text
        #         if '智慧树警告' in warning:
        #             print('删除中')
        #             remover = WebDriverWait(self.driver, 30, 0.2).until(
        #                 lambda driver: driver.find_element_by_class_name("el-dialog"))
        #             self.driver.execute_script('arguments[0].remove()', remover)
        #     else:
        #         break
        subchapterId = subchapter.find_element_by_css_selector('b.pl5').text
        subchapterName = subchapter.find_element_by_css_selector('span.catalogue_title').text

        try:
            subchapter.find_element_by_css_selector('span.catalogue_title').click()
        except:
            print('出现异常，正在检查')
        fail = 0
        lastState = '0:00'
        while True:
            # 查找 弹框 元素 存在
            if driver.find_elements_by_css_selector('div.el-dialog'):
                quiz = driver.find_element_by_css_selector('div.el-dialog')
                test = 0
                try:
                    quizformat = driver.find_element_by_css_selector('span.title-tit').text
                    print('出现随机题目')
                    # 确认 弹窗 为 题目
                    test = 1
                except:
                    pass
                if test == 1:
                    # 判断题目类型
                    if '多选题' in quizformat:
                        print('识别为多选题')
                        self.doMulti(quiz,driver)
                    elif '单选题' in quizformat:
                        print('识别为单选题')
                        self.doSingle(quiz,driver)
                    elif '判断题' in quizformat:
                        print('识别为判断题')
                        self.doJudge(quiz,driver)
                    if first == 1:
                        subchapter.find_element_by_css_selector('span.catalogue_title').click()
                        first = 0
            # 判断任务进度
            currentState = subchapter.find_element_by_css_selector('span.progress-num').text
            if lastState == currentState:
                fail += 1
            lastState = currentState
            # 六次进度没有增长
            if fail >= 6:
                print('检测到进度未变化，正在检查播放按钮')
                self.driver.find_element_by_css_selector('div#playButton').click()
                print('重试成功')
                fail = 0
            # 判断任务完成
            try:
                subchapter.find_element_by_css_selector('b.time_icofinish')
                print('第{}节 {} 已完成'.format(subchapterId, subchapterName))
                fail = 0
                lastState = '0:00'
                break
            except:
                pass
            time.sleep(5)


    def findCourse(self):
        # self.option.add_argument('blink-settings=imagesEnabled=true')  # 不加载图片, 提升速度，但无法显示二维码
        # self.option.add_argument('--headless')
        # self.option.add_argument('--disable-extensions')
        # self.option.add_argument('--disable-gpu')
        # self.option.add_argument('--no-sandbox')
        # self.driver = webdriver.Chrome(chrome_options=self.option)
        # print('正在打开首页')
        # self.driver.get('https://www.zhihuishu.com/')
        # print('打开首页成功')
        # print('正在加载Cookies')
        # with open('saves/usercookies.json','r') as f:
        #     cookies = json.load(f)
        #     for cookie in cookies:
        #         self.driver.add_cookie(cookie)
        # print('Cookies加载成功')
        # print('正在打开课程页')
        # self.driver.get('https://onlineh5.zhihuishu.com/onlineWeb.html#/studentIndex')
        # WebDriverWait(self.driver, 30, 0.2).until( lambda driver: driver.find_element_by_class_name("courseName"))
        print('寻找课程')
        courseImg = self.driver.find_element_by_class_name('courseName')
        courseImg.click()
        print('打开课程')
        WebDriverWait(self.driver, 30, 0.2).until( lambda driver: driver.find_element_by_class_name("catalogue_title3"))
        print('搜索所有章节')
        chapters = self.driver.find_elements_by_class_name('list')
        currentC = 1
        for chapter in chapters:
            chapterName = chapter.find_element_by_css_selector('span.catalogue_title')
            print('开始学习第{}章:'.format(currentC)+chapterName.text)
            subchapters = chapter.find_elements_by_css_selector('li.clearfix')[1:]
            for subchapter in subchapters:
                subchapterId = subchapter.find_element_by_css_selector('b.pl5').text
                subchapterName = subchapter.find_element_by_css_selector('span.catalogue_title').text
                if subchapter.find_elements_by_css_selector('b.time_icofinish'):
                    print('第{}节 {} 已完成 跳过小节'.format(subchapterId,subchapterName))
                elif subchapter.find_elements_by_css_selector('span.progress-num'):
                    subchapterProgress = subchapter.find_element_by_css_selector('span.progress-num').text
                    print('第{}节 {} 已完成{} 开始学习'.format(subchapterId,subchapterName,subchapterProgress))
                    subchapterTime = subchapter.find_element_by_css_selector('span.time').text
                    print('视频总长度 {}'.format(subchapterTime))
                    self.watchVideo(subchapter,self.driver)
                else:
                    unfound = 0
                    print('第{}节 {} 无进度 开始学习'.format(subchapterId, subchapterName))
                    try:
                        subchapterTime = subchapter.find_element_by_css_selector('span.time').text
                    except:
                        print('第{}节 {} 无法学习 跳过'.format(subchapterId, subchapterName))
                        unfound = 1
                    if unfound == 1:
                        pass
                    else:
                        print('视频总长度 {}'.format(subchapterTime))
                        self.watchVideo(subchapter,self.driver)



            currentC += 1





if __name__ == '__main__':
    lo = Login()
    lo.showQRcode()