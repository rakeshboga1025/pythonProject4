age=20

if age >= 18:
    print("Eligible for vote")
else:
    print("not eligible for vote")

num =10

if num % 2==0:
    print("number is even")
else:
    print("number is odd")

print(list(range(1,20,3)))

i=1
while i<=10:
    print(i)
    i=i+1
print("DONE")

for i in range(10):
    print(i)


for i in range(10):
    if i==5:
       break
print(i)

for i in range(10):
    if i==5:
        continue
print(i)


print(max(10,20,50,40,100,55))
print(min(10,20,50,40,100,55))

f=1
n=5
for i in range(1, n+1):
    f=f*i
print(f)