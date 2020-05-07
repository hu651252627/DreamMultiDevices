# -*- coding: utf-8 -*-
__author__ = "无声"

import unittest
from DreamMultiDevices.tools import  Screencap
from airtest.core.api import *
from tools.TimeOut import Timeout
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import time


_print = print
def print(*args, **kwargs):
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), *args, **kwargs)

def test_backward(self):
    poco = AndroidUiautomationPoco()
    while poco("cn.chengyu.love:id/closeBtn").exists():
        poco("cn.chengyu.love:id/closeBtn").click()

def test_backward1(self):
    poco = AndroidUiautomationPoco()
    while poco("cn.chengyu.love:id/backImageView").exists():
        poco("cn.chengyu.love:id/backImageView").click()

def Main(devices):
    print("{}进入unittest".format(devices))
    class TC100(unittest.TestCase):
        u'''测试用例101的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''

            print("我是TC101的test_01_of_101方法")
        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            print("我是setUp，在每条用例之前执行")
        @Timeout.timeout(10)
        def test_phone_login(self):
            poco = AndroidUiautomationPoco()
            poco(text="手机号登录").click()
            if poco(text="手机验证码登录").exists():
                poco(text="手机验证码登录").click()
            poco("cn.chengyu.love:id/phoneEditText").set_text("17096852112")
            poco("cn.chengyu.love:id/codeEditText").set_text("112233")
            poco(text="登录").click()
            sleep(2)
            value = poco("cn.chengyu.love:id/normalRoomTv").attr("text")
            assert_equal(value, "普通房间", "登录成功")
            t = 1
            self.assertEquals(1, t)

         # 身份认证
        def test_identity_authentication(self):
            poco = AndroidUiautomationPoco()
            poco("cn.chengyu.love:id/idCardLay").click()
            poco("cn.chengyu.love:id/realNameEt").set_text("孙雪")
            poco("cn.chengyu.love:id/cardNoEt").set_text("210303198412082729")
            poco("cn.chengyu.love:id/submitBtn").click()
            sleep(2)
            value = poco("cn.chengyu.love:id/submitBtn").attr("text")
            assert_equal(value, "确定", "身份认证成功")
            poco(text="确定").click()
            t = 1
            self.assertEquals(1, t)
        # def test_02_of_101(self):
        #     u'''用例test_02_of_101的操作步骤'''
        #     # 每个函数里分别实例poco，否则容易出现pocoserver无限重启的情况
        #     poco = UnityPoco()
        #     print("我是TC102的test_02_of_101方法")
        #     Screencap.GetScreen(time.time(), devices, "test_02_of_101的描述")
        #     t = 1
        #     self.assertEquals(2, t)


        def tearDown(self):
            u'''这里放需要在每条用例后执行的部分'''
            print("我是tearDown，在每条用例之后执行")

        @classmethod
        def tearDownClass(self):
            u'''这里放需要在所有用例后执行的部分'''
            pass

    srcSuite = unittest.makeSuite(TC100)
    return srcSuite