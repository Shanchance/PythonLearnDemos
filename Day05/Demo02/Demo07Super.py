class A:
    def say(self):
        print("A:",self)
class B(A):
    def say(self):
        A().say()
        super().say()
        print("B:",self)
b = B()
b.say()
