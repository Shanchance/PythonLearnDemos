class A:
    def say(self):
        print("hello world")
class B:
    def __init__(self,a):
        self.a = a
a = A()
b = B(a)
b.a.say()

