# Break continue

for i in range(1,10):
    if i==5:
        break
    print(i)
print("program exited")

for i in range(10):
    if i==8:
        continue
    print(i)
print("Done")

for i in range(1,10):
    if i==3 or i==5 or i==7:
        continue
    print(i)
print("done")