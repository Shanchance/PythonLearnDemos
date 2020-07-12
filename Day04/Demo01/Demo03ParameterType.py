def test01(a,b,c):
    print("a:{0}，b:{1}，c:{2}".format(a,b,c))

def test02(a,c,b=3):
    print("a:{0}，b:{1}，c:{2}".format(a,b,c))


test01(1,3,5)
test01(c=3,a=2,b=6)

test02(2,4)