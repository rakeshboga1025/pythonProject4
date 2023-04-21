# ways of creating string demo
s="welcome"
s='welcome'
s=str('welcome')
s=str("welcome")


# creating empty string varibales

name=' '
name=" "
name=str( )

str1='welcome'
print(id(str1))
str1=str1+"to python"

# Ex=3    * and * with string
str='welcome'
print(str+'programming') #concatination
print(3*'welcome')


# Ex=4  Slicing
str='welcome'
    #0123456
    #7654321
print(str[1:3]) # el
print(str[:6])   #welcom
print(str[2:])   #lcome
print(str[1:-1])  #elcom
print(str[1:-2])   #elco

# max() mIn()  len()

print(max("RAKESH"))
print(max("HRushitha"))

print(len("RakesHRushith"))

# in , not in operators
s= "welcome"

print("come" in s)
print("ing" not in s)

