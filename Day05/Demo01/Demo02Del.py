class Person:
    def __del__(self):
        print("{0}被删除".format(self))

p1 = Person()
p2 = Person()