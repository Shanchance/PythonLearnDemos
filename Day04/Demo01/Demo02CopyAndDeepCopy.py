import copy
def testCopy():
    """
    测试浅拷贝
    :return:
    """
    a = [20,30,[3,4]]
    b = copy.copy(a)
    print("a:",a)
    print("b:",b)
    print("---------浅拷贝---------")
    b.append(40)
    b[2].append(5)
    print("a:", a)
    print("b:", b)

def testDeepCopy():
    """
    测试深拷贝
    :return:
    """
    a = [20,30,[3,4]]
    b = copy.deepcopy(a)
    print("a:",a)
    print("b:",b)
    print("---------深拷贝---------")
    b.append(40)
    b[2].append(5)
    print("a:", a)
    print("b:", b)

testCopy()
print("============================")
print("============================")
testDeepCopy()