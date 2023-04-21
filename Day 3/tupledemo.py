mytuple=("apple","banana","orange")
print(mytuple)

# access tuple items
print(mytuple[1])

mytuple=("apple","banana","orange",'kiwi',"mango")
print(mytuple[2:4])
print(mytuple[-4:-2])

mytuple=("apple","banana","orange",'kiwi',"mango")
mylist=list(mytuple)
mylist.insert(2,"lemon")
mytuple=tuple(mylist)
print(mytuple)

mytuple=("apple","banana","orange",'kiwi',"mango")
for i in mytuple:
    print(i)