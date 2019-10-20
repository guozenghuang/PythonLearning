import re


def main():
    names = ["var", "var1", "var_", "_var", "!var", "1var", "var!", "va_r1", "var#", "va@#r"]
    for name in names:
        ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9]*$", name)
        if ret:
            print("%s 符合变量规则, 通过正则匹配出来的数据是 %s" % (name, ret.group()))
        else:
            print("%s 不符合变量规则" % name)


if __name__ == "__main__":
    main()
