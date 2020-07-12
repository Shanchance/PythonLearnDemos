#工厂方法模式
class CarFactory:
    def create_car(self,bread):
        if bread == "奔驰":
            return Benz()
        elif bread == "宝马":
            return BMW()
        elif bread == "比亚迪":
            return BYD()
        else:
            print("小众车，无法创建")

class Benz:
    def __init__(self):
        print("奔驰生产了")
class BMW:
    def __init__(self):
        print("宝马生产了")
class BYD:
    def __init__(self):
        print("比亚迪生产了")

factory = CarFactory()
factory.create_car("奔驰")
factory.create_car("宝马")
factory.create_car("比亚迪")
factory.create_car("劳斯莱斯")

