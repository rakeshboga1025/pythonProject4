num=5
factorial=1
if num<0:
    print("the factorial number is not an negative")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of",num,"is",factorial)

