"""
   *表示可变参数
   *元组
   **字典
   """

def test01(a,b,*c):
    print("a:{0},b:{1},c:{2}".format(a,b,c))

def test02(a,b,**c):
    print("a:{0},b:{1},c:{2}".format(a,b,c))

def test03(*a,b,c):
    """
    可变参数后的参数，必须强制命名
    :param a:
    :param b:
    :param c:
    :return:
    """
    print("a:{0},b:{1},c:{2}".format(a,b,c))


test01(1,4,6,5,7,8)
test02(3,5,name="shancx",age=22)
test03(3,5,6,b=3,c=4)