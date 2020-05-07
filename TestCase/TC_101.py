# -*- coding: utf-8 -*-
__author__ = "无声"

import unittest
from DreamMultiDevices.tools import  Screencap
from airtest.core.api import *
from TestCase.My_tool import *
from tools.TimeOut import Timeout
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import time


_print = print
def print(*args, **kwargs):
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), *args, **kwargs)

def backward(self):
    poco = AndroidUiautomationPoco()
    while poco("cn.chengyu.love:id/closeBtn").exists():
        poco("cn.chengyu.love:id/closeBtn").click()

def backward1(self):
    poco = AndroidUiautomationPoco()
    while poco("cn.chengyu.love:id/backImageView").exists():
        poco("cn.chengyu.love:id/backImageView").click()

def Main(devices):
    print("{}进入unittest".format(devices))
    class TC101(unittest.TestCase):
        u'''测试用例101的集合'''

        @classmethod
        def setUpClass(self):
            u''' 这里放需要在所有用例执行前执行的部分'''
            #登录
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
            print("我是TC101的test_01_of_101方法")
        def setUp(self):
            u'''这里放需要在每条用例前执行的部分'''
            # time.sleep(4)

            print("我是setUp，在每条用例之前执行")

        @Timeout.timeout(10)
         # 身份认证
        def identity_authentication(self):
            poco = AndroidUiautomationPoco()
            poco("cn.chengyu.love:id/idCardLay").click()
            poco("cn.chengyu.love:id/realNameEt").set_text("孙雪")
            poco("cn.chengyu.love:id/cardNoEt").set_text("210303198412082729")
            poco("cn.chengyu.love:id/submitBtn").click()
            sleep(2)
            value = poco("cn.chengyu.love:id/submitBtn").attr("text")
            assert_equal(value, "确定", "身份认证成功")
            poco(text="确定").click()

        # 实名认证
        def real_name_authentication(self):
            poco = AndroidUiautomationPoco()
            # 在我的界面点击实名认证按钮
            poco("cn.chengyu.love:id/nameLay").click()
            # 上传身份证正面
            poco("cn.chengyu.love:id/frontCardImg").click()
            poco("cn.chengyu.love:id/dialog_tv_select").click()
            poco("cn.chengyu.love:id/check_view")[0].click()
            # 使用按钮
            poco("cn.chengyu.love:id/button_apply").click()
            time.sleep(2)
            # 上传身份证国徽面
            poco("cn.chengyu.love:id/backCardImg").click()
            poco("cn.chengyu.love:id/dialog_tv_select").click()
            poco("cn.chengyu.love:id/check_view")[1].click()
            # 使用按钮
            poco("cn.chengyu.love:id/button_apply").click()
            time.sleep(2)

            # 上传手持身份证
            poco("cn.chengyu.love:id/takeCardImg").click()
            poco("cn.chengyu.love:id/dialog_tv_select").click()
            poco("cn.chengyu.love:id/check_view")[2].click()
            # 使用按钮
            poco("cn.chengyu.love:id/button_apply").click()
            time.sleep(2)
            poco("cn.chengyu.love:id/confirmBtn").click()
            time.sleep(5)
            value = poco("cn.chengyu.love:id/processTv1").attr("text")
            assert_equal(value, "预计24小时内返回结果", "实名认证填写成功")
            # 点击返回按钮
            poco("cn.chengyu.love:id/closeBtn").click()

        # 我的动态
        # 发布有文字有话题的动态
        def many_picture_zone(self):
            poco = AndroidUiautomationPoco()
            # 点击进入动态界面
            poco("cn.chengyu.love:id/trendsMoreImageView").click()
            # 点击发布动态
            poco("cn.chengyu.love:id/addTrendsLayout").click()
            # 选择图片
            poco("cn.chengyu.love:id/tvCheck")[1].click()
            poco("cn.chengyu.love:id/picture_tv_ok").click()
            # 添加文字
            poco("cn.chengyu.love:id/contentEditText").set_text("我是测试发布图片动态")
            # 再次添加一张图片
            poco("cn.chengyu.love:id/addImageView").click()
            poco("cn.chengyu.love:id/tvCheck")[2].click()
            poco("cn.chengyu.love:id/picture_tv_ok").click()
            # 选择话题
            poco("cn.chengyu.love:id/trendsMoreImageView").click()
            poco(text="#冬天的记忆").click()
            # 添加地点
            poco("cn.chengyu.love:id/addressTextView").click()
            poco("cn.chengyu.love:id/titleTextView")[0].click()
            # 发布
            poco("cn.chengyu.love:id/submitTextView").click()
            sleep(5)
            # 返回
            poco("cn.chengyu.love:id/closeBtn").click()
            sleep(2)
        # 发布一个全部都有的视频动态
        def video_zone(selg):
            poco = AndroidUiautomationPoco()
            # 点击进入动态界面
            poco("cn.chengyu.love:id/trendsMoreImageView").click()
            # 点击发布动态
            poco("cn.chengyu.love:id/addTrendsLayout").click()
            # 选择拍摄
            poco("cn.chengyu.love:id/tvCamera").click()
            # 选择录视频按钮
            poco("cn.chengyu.love:id/picture_tv_video").click()
            # 录制视频
            poco("com.android.camera:id/shutter_button").click()
            sleep(5)
            # 停止录制
            poco("com.android.camera:id/shutter_button").click()
            # 确认视频
            poco("com.android.camera:id/btn_done").click()
            poco("cn.chengyu.love:id/picture_tv_ok").click()

            # 添加文字
            poco("cn.chengyu.love:id/contentEditText").set_text("我是测试发布视频动态我是测试发布视频动态")
            # 选择话题
            poco("cn.chengyu.love:id/trendsMoreImageView").click()
            poco(text="#冬天的记忆").click()
            # 添加地点
            poco("cn.chengyu.love:id/addressTextView").click()
            poco("cn.chengyu.love:id/titleTextView")[0].click()
            # 发布
            poco("cn.chengyu.love:id/submitTextView").click()
            sleep(5)
            # 返回
            try:
                poco("cn.chengyu.love:id/closeBtn").wait_for_appearance(timeout=120)
            except:
                print("none")
            poco("cn.chengyu.love:id/closeBtn").click()
            sleep(2)
        # 基本资料
        def basic_data(self):
            poco = AndroidUiautomationPoco()
            # 进入基本资料
            poco("cn.chengyu.love:id/basicInfoLay").click()
            # 交友心声
            poco("cn.chengyu.love:id/singelSignTv").set_text("我是男一号")
            # 修改昵称
            poco("cn.chengyu.love:id/nickNameLay").click()
            poco(name=signEt).set_text("夏雨荷")
            poco(text="确定").click()
            # 修改出生年月
            poco(name=birthDayLay).click()
            poco(name=year_pv).swipe([0.2, 0.2])
            poco(text="确定").click()
            # 学历
            poco(name=educationLay).click()
            poco(text="确定").click()
            # 婚姻状况
            poco(name=marriedStatusLay).click()
            poco(text="确定").click()
            # 身高
            poco(name=heightLay).click()
            poco(text="确定").click()
            # 月收入
            poco(name=incomeLay).click()
            poco(text="确定").click()
            # 职业
            poco(name=professionLay).click()
            poco(text="确定").click()

            # 移动让更多资料出现
            poco(name="android.widget.LinearLayout").swipe([-0.5, -0.5])
            # 住房情况
            poco(name=houseLay).click()
            poco(text="确定").click()
            # 魅力部位
            poco(name=charmingLay).click()
            poco(name=charmCb)[0].click()
            poco(name=charmCb)[1].click()
            poco(text="确定").click()
            # 血型
            poco(name=bloodTypeLay).click()
            poco(text="确定").click()
            # 婚后与父母同住
            poco(name=liveWithParentLay).click()
            poco(text="确定").click()
            # 婚前同居
            poco(name=cohabitationLay).click()
            poco(text="确定").click()
            # 点击保存
            poco(text="保存").click()
            sleep(2)

        # 征友条件
        def acquisition_conditions(self):
            poco = AndroidUiautomationPoco()
            poco(name=conditionLay).click()

            # 所在地
            poco(name=locationLay).click()
            poco(name=locationChooser).swipe([-0.5, -0.5])
            poco(text="确定").click()
            # 年龄范围
            poco(name=ageRangeLay).click()
            poco(name=startAgeChooser).swipe([-0.5, -0.4])
            poco(name=endAgeChooser).swipe([-0.5, -0.5])
            poco(text="确定").click()
            # 身高
            poco(name=heightLay).click()
            poco(name=startHeightChooser).swipe([-0.5, -0.4])
            poco(name=endHeightChooser).swipe([-0.5, -0.5])
            poco(text="确定").click()
            # 最低学历
            poco(name=lowestEduLay).click()
            poco(text="确定").click()
            # 月收入
            poco(name=incomeLay).click()
            poco(text="确定").click()
            # 点击保存
            poco(text="保存").click()
            sleep(2)

        # 我的标签
        def my_label(self):
            poco = AndroidUiautomationPoco()
            poco(name=tagLay).click()
            # 选择性格
            poco(text="成熟稳重").click()
            poco(text="有责任心").click()
            poco(text="幽默").click()
            # 选择爱好
            poco(text="自驾游").click()
            poco(text="刷抖音").click()
            # 点击保存
            poco(text="保存").click()
            sleep(2)

        # 邀请用户
        def invitation(self):
            poco = AndroidUiautomationPoco()
            poco(inviteLay).swipe([0, -0.5])
            # 分享给好友
            poco(inviteLay).click()
            poco(name="分享给微信好友").click()
            sleep(2)
            poco(name="com.tencent.mm:id/dsx").click()
            sleep(2)
            poco(text="分享").click()
            sleep(2)
            poco(text="返回诚遇").click()
            sleep(5)
            # 分享到朋友圈
            poco(name="分享到微信朋友圈").click()
            try:
                poco(text="发表").wait_for_appearance(timeout=120)
            except:
                print("none")
            poco(text="发表").click()
            sleep(5)
            backward()

        # 我的玫瑰
        def my_rose(self):
            poco = AndroidUiautomationPoco()
            poco(inviteLay).swipe([0, -0.5])
            poco(name=roseLay).click()
            # 点击充值金额1元
            poco(name=buyRose1).click()
            poco(name=wxPayLay).click()
            poco(name=m1).click()
            poco(text="退出").click()
            # 点击充值金额6元
            poco(name=buyRose6).click()
            poco(name=wxPayLay).click()
            poco(name=m1).click()
            poco(text="退出").click()
            # 点击充值金额30元
            poco(name=buyRose30).click()
            poco(name=wxPayLay).click()
            poco(name=m1).click()
            poco(text="退出").click()
            # 点击充值金额108元
            poco(name=buyRose108).click()
            poco(name=wxPayLay).click()
            poco(name=m1).click()
            poco(text="退出").click()
            # 点击充值金额288元
            poco(name=buyRose288).click()
            poco(name=wxPayLay).click()
            poco(name=m1).click()
            poco(text="退出").click()
            # 点击充值金额500元
            poco(name=buyRose500).click()
            poco(name=wxPayLay).click()
            poco(name=m1).click()
            poco(text="退出").click()
            # 点击充值金额1000元
            poco(name=buyRose1000).click()
            poco(name=wxPayLay).click()
            poco(name=m1).click()
            poco(text="退出").click()

            poco(name=buyRose1000).swipe([-0.5, -0.5])

            # 点击充值金额2000元
            poco(name=buyRose2000).click()
            poco(name=wxPayLay).click()
            poco(name=m1).click()
            poco(text="退出").click()
            # 点击充值金额3000元
            poco(name=buyRose3000).click()
            poco(name=wxPayLay).click()
            poco(name=m1).click()
            poco(text="退出").click()

            poco(name=buyRose1000).swipe([0, 0.5])
            poco(name=closeBtn).click()

        # 购买vip
        def vip(self):
            poco = AndroidUiautomationPoco()
            poco(inviteLay).swipe([0, -0.5])
            poco(name=vipLay).click()
            # 点击成为会员
            poco(name=buyVipTv).click()
            poco(name=closeBtn).click()
            sleep(2)
            poco(name=confirmBtn).click()
            poco(name=closeBtn).click()
            sleep(1)
            # 查看免费卡
            poco(name=checkCardTv).click()
            poco(name=closeBtn).click()
            sleep(1)
            # 领取相亲卡
            poco(name=receiverCardTv).click()
            poco(name=closeBtn).click()
            sleep(1)
            # 领取好友亲卡
            poco(name=receiverCardTv2).click()
            poco(name=closeBtn).click()
            sleep(1)
            # 跳转到分享好友界面
            poco(name=adverImg).click()
            try:
                poco(name=closeBtn).wait_for_appearance(timeout=120)
            except:
                print("none")
            poco(name=closeBtn).click()
            # 充值30天
            poco(name=confirmBtn).click()
            sleep(1)
            poco(name=vip1Lay).click()
            poco(name=confirmBtn).click()
            poco(name=wxPayLay).click()
            poco(name=m1).click()
            poco(text="退出").click()
            sleep(2)
            # 充值90天
            poco(name=vip2Lay).click()
            poco(name=confirmBtn).click()
            poco(name=wxPayLay).click()
            poco(name=m1).click()
            poco(text="退出").click()
            sleep(2)
            # 充值360天
            poco(name=vip3Lay).click()
            poco(name=confirmBtn).click()
            poco(name=wxPayLay).click()
            poco(name=m1).click()
            poco(text="退出").click()
            sleep(2)
            # 返回
            poco(name=closeBtn).click()
            poco(name=closeBtn).click()

        # 我的钱包
        def my_wallet(self):
            poco = AndroidUiautomationPoco()
            poco(walletLay).click()
            # 查看收入记录
            poco(text="收入记录").click()
            poco(closeBtn).click()
            poco(text="点击提现").click()
            if poco(text="取消").exists():
                poco(text="取消").click()
            poco(text="兑换玫瑰").click()
            poco(text="兑换记录").click()
            sleep(1)
            backward()

        # 投诉与反馈
        def feedback(self):
            poco = AndroidUiautomationPoco()
            poco(inviteLay).swipe([0, -0.5])
            poco(name=adviceLay).click()
            # 发送文字
            poco(name=chat_message_input).set_text("客服在不在，我有问题要反馈")
            poco(name=send_btn).click()

            # 发送表情
            poco(name=face_btn).click()
            poco(name="cn.chengyu.love:id/face_image").click()
            poco(name=send_btn).click()

            # 发送照片
            poco(name=more_btn).click()
            poco(name=imageView).click()
            poco(name="com.android.documentsui:id/thumbnail")[0].click()
            # 返回
            poco(name=closeBtn).click()

        # 设置
        def install_black_listLay(self):
            poco = AndroidUiautomationPoco()
            poco(inviteLay).swipe([0, -0.5])
            poco(name=settingLay).click()
            # 黑名单
            poco(name=blackListLay).click()
            sleep(2)
            poco(name=closeBtn).click()
            poco(name=closeBtn).click()

        # 退出账号
        def install_logout(self):
            poco = AndroidUiautomationPoco()
            poco(name="cn.chengyu.love:id/inviteLay").swipe([0, -0.5])
            poco(name=settingLay).click()
            # 黑名单
            poco(name=logoutBtn).click()
            sleep(2)

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

    srcSuite = unittest.makeSuite(TC101)
    return srcSuite