
def print_name(is_Chinese,fName,lName):
    """
    内部函数可以定义，在函数内部声明，使用。只为该函数服务
    :param is_Chinese:
    :param fName:
    :param lName:
    :return:
    """
    def f(fName,lName):
        print("{0}{1}".format(fName, lName))
    if is_Chinese == True:
        f(fName,lName)
    else:
        f(lName,fName)

print_name(True,"单","想")
print_name(False,"James","Li")