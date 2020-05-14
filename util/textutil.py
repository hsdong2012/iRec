# -*- coding:utf-8 -*-

import re

"""
功能:
* 1, 对姓名字符串进行解析，获得姓名列表
* 2, 校验email格式
* 3, 校验手机号码格式
* 4, 校验密码格式
"""

class TextUtil(object):
    # 采用replace/split方法以中文/英文逗号或空格解析姓名字符中, 有些麻烦!
    @classmethod
    def parseNamesByReplace(cls, strNames):
        # 处理多行文本，将换行符替换为英文逗号
        if "\n" in strNames:
            strNames = strNames.replace("\n", ",")

        # 将中文逗号替换为英文逗号
        if "，" in strNames:
            strNames = strNames.replace("，", ",")

        # 空格替换为英文逗号
        if " " in strNames:
            strNames = strNames.replace(" ", ",")

        # 用英文逗号为分隔符分隔字符串, 较为简单没有使用正则表达式
        nameList = strNames.split(",")
        nameList = [item for item in nameList if len(item) > 0]

        return nameList

    # 采用正则表达式以中文/英文逗号或空格解析姓名字符中
    @classmethod
    def parseNames(cls, strNames):
        # 如果多行文本，将换行符替换为英文,
        if "\n" in strNames:
            strNames = strNames.replace("\n", ",")

        # 姓名只需要一个或多个连续字符匹配
        regx = r"\w+"
        nameList = re.findall(regx, strNames) # 匹配字符串，获得姓名列表

        return nameList

    # 校验email
    @classmethod
    def verifyEmail(cls, strEMail):
        if re.match(r'^(\w)+(\.\w+)*@(\w)+((\.\w+)+)$', strEMail):
            return True
        else:
            return False

    # 校验手机号, 数字11位,需要以13/5/6/7/8打头, 长度需要为11位
    @classmethod
    def verifyPhoneNum(cls, strPhoneNum):
        if re.match(r"^1[35678]\d{9}$", strPhoneNum):
            return True
        else:
            return False

    # 校验密码, 需要3-8位之间的字符
    @classmethod
    def vefifyPassword(cls, password):
        if re.match(r"^\w{3,8}", password):
            return True
        else:
            return False

if __name__ == '__main__':
    names = TextUtil.parseNames("""
            张三 李四, 王五，
            周七 
             赵六""")
    print(names)
    print(TextUtil.verifyEmail("hello@itcase.cn"))
    print(TextUtil.verifyPhoneNum("13812791891"))
    print(TextUtil.vefifyPassword("admin"))




