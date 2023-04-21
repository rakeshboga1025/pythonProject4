mylist=[0,1,22,4,0,5,6,9,7]
#mylist[0],mylist[-1]=mylist[-1],mylist[0]
#print(mylist)

first=mylist.pop(0)
last=mylist.pop(-1)

mylist.insert(0,last)
mylist.append(first)

print(mylist)