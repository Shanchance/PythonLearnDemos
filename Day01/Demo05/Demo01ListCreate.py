list1 = [1,2,3,"sss"]
print(list1)
list1.append("shanchance")
print(list1)
print(list1[2],list1[3])
print("=================")

list2 = list()
print(list2)

list3 = list("shanchance")
print(list3)

list4 = list(range(10))
print(list4)
list5 = list(range(2,20,2))
print(list5)
list6 = list(range(20,0,-2))
print(list6)
list7 = list(range(-20,0,2))
print(list7)

a = [i*2 for i in range(5)]
print(a)
b = [i for i in range(100) if(i%5==0)]
print(b)