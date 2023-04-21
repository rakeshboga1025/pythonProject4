arr=[5,1,2,10,15,12,80,40]
n=(len(arr))
print(len(arr))

max=arr[0]
for i in range(1,n):
    if arr[i]>max:
        max=arr[i]

print(max)



min=arr[0]

for i in range(1,n):
    if arr[i]<min:
        min=arr[i]

print(min)