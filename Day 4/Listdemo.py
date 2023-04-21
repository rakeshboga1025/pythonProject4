mylist=('apple', 'banana', 'orange')

print(mylist[0])
print(mylist[1])
print(mylist[-1])
print(mylist[-2])

mylist1=['apple', 'banana', 'orange']
for i in mylist1:
    print(i)

mylist2=(10,60,20,40,500)
strs=['car','bus','auto']
mylist4=('nokia','samsung','mi')

print(mylist2)
print(mylist4)

strs.sort()
print(strs)


# change item value
mylist5=["apple","lemon","karzura"]
print(mylist5)
mylist5[0]="orange"
print(mylist5)

# range of index
mylist5=["apple","lemon","karzura",'cherry','melon']
print(mylist5)
print(mylist5[2:-1])

mylist5=["apple","lemon","karzura",'cherry','melon']
for i in mylist5:
    print(i)

mylist5 = ["apple", "lemon", "karzura", 'cherry', 'melon']
if 'apple' in mylist5:
    print('apple is present')
else:
    print('apple is not present')

# list length
mylist5 = ["apple", "lemon", "karzura", 'cherry', 'melon']
print(len(mylist5))

# add items
mylist5 = ["apple", "lemon", "karzura", 'cherry', 'melon']
mylist5.append('orange')
print(mylist5)

mylist5.insert(1,"car")
print(mylist5)


mylist6=list(mylist5)
print(mylist6)

# combine/joins lists

list1=["a","b","c","d"]
list2=["1","2","3","4"]
list3=list2+list1
print(list3)

list1=["a","b","c","d"]
list2=["1","2","3","4"]
for i in list2:
    list1.append(i)
print(list1)
