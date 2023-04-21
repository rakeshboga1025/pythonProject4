mylist=[0,1,22,4,0,5,6,9,7]
print(mylist)

pos1=mylist[1]
pos2=mylist[6]
mylist[pos1],mylist[pos2]=mylist[pos2],mylist[pos1]
print(mylist)


