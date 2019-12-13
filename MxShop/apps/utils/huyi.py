import http.client
import urllib
import json


class HuYi(object):
    def __init__(self, account, password):
        self.host = "106.ihuyi.com"
        self.sms_send_uri = "/webservice/sms.php?method=Submit"

        # 查看用户名 登录用户中心->验证码通知短信>产品总览->API接口信息->APIID
        self.account = account
        # 查看密码 登录用户中心->验证码通知短信>产品总览->API接口信息->APIKEY
        self.password = password

    def send_sms(self, code, mobile):
        params = urllib.parse.urlencode(
            {'account': self.account,
             'password': self.password,
             'content': "您的验证码是：{code}。请不要把验证码泄露给其他人。".format(code=code),
             'mobile': mobile,
             'format': 'json'})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = http.client.HTTPConnection(self.host, port=80, timeout=30)
        conn.request("POST", self.sms_send_uri, params, headers)
        response = conn.getresponse()
        re_dict = json.load(response)
        conn.close()
        return re_dict



