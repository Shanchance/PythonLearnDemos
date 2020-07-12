class Studnet:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def say_score(self):
        print("{0}的分数是：{1}".format(self.name,self.score))

ss = Studnet("单长喜",100)
ss.say_score()
