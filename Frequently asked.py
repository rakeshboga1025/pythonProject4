x=10
y=20

print(x)
print(y)

x,y=y,x

print(x)
print(y)



mylist=(10,20,5,16,18)

ele=5

for i in mylist:
    if(i==ele):
        print("element was found")
else:
        print("element not found")
