class Man:
    def eat(self):
        print("饿了，想吃饭饭")
class Chinese(Man):
    def eat(self):
        print("中国人用筷子")
class English(Man):
    def eat(self):
        print("英国人用叉子")
def man_eat(m):
    if isinstance(m,Man):
        m.eat()
    else:
        print("不是人，不能吃饭")

man_eat(Chinese())
man_eat(English())
man_eat(Man)
