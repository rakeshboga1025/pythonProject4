mylist=[0,1,22,4,0,5,6,9,7,0,5.22,4,4,4,4]
n=len(mylist)

x=4
count=0
for ele in mylist:
    if(ele==x):
        count=count+1
#print("{} has occured {} times".format(x,count))

x=4
print("{} has occured {} times".format(x,count(x)))