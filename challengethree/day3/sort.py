#list to be sorted as even,odd and strings
list = ([2,0,6,5,1,7,'z','a'])
#sort int modulus 2 and returns even numbers
intList=sorted([n for n in list if type(n) is int and n % 2 == 0])
#sort int if not modulus 2 and return odd numbers
intListodd=sorted([n for n in list if type(n) is int and n % 2 != 0])
#return strings
strList=sorted([n for n in list if type(n) is str ])

print("Even:", intList,"odd:", intListodd,"character:", strList)
