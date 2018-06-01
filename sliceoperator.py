str1= "helloworld"
str2= 'this is an example operator'
num='12345678990'

print (str1, type(str1), id(str1))

print ('Range slice and left to right indexing', str1[0])

print ("")
print('Range slice and right to left indexig', str1[-1])

print(str1[0:5])
print("")

print(num, type(num), len(num), id(num))
print(num[0::2])

#string concatenation
print("updated string", str1[:6] + "planet")
print("updated string", str1[:12] + "Perl")

#formating string

print("your name is %s and your account id is %d" %("khandu", 12345))

print(str1, len(str1))
print(str1[0])
print(str1[9])
print(str1[-1])
print(str1[-6])

print (str1[2:6])
print (str1[:5])

print (str1 *3)

