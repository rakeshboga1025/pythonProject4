F=open('C:\Documents\RakesH.txt','w')

F.write("This is my first comment \n")
F.write("This is my second comment\n")
F.write("This is my third comment\n")
F.write("This is my fourt comment\n")
F.write("This is my fifth comment\n")

F.close()

F=open('C:\Documents\RakesH.txt', 'r')
print(F.read())

F=open('C:\Documents\RakesH.txt', 'r')
print(F.readlines())

F=open('C:\Documents\RakesH.txt', 'r')
print(F.readline())
