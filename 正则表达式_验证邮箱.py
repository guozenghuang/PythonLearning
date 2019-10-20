import re


def main():
    mail = input("请输入163或qq邮箱地址:")

    ret = re.match(r"^[a-zA-Z0-9]{6,20}@(163|qq)\.com$", mail)
    #ret = re.match(r"<(/w*)><(/w*)>*<\2><\1>$", html_str) # 1与前一个括号相同 2与第二个括号相同
    #ret = re.match(r"<(?P<p1>/w*)><(?P<p2>/w*)>*<\?P=p2><\?P=p1>$", html_str) # p1与前一个括号相同 p2与第二个括号相同

    if ret:
        print("输入的qq邮箱地址正确")
        print("输入的邮箱地址是:%s" % ret.group())
        print("输入的邮箱类型是:%s邮箱" % ret.group(1))
    else:
        print("输入的邮箱地址有误请输入6-20为qq邮箱名并以@qq.com结尾")


if __name__ == "__main__":
    main()
