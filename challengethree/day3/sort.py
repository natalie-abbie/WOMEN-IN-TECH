def list_sort(n):
   
    intList = []
    intListodd = []
    strList = []
    #sort int modulus 2 and returns even numbers
    for a in n: 
        #checking for even and odd numbers
        if type(a) is int and a % 2 == 0:
            intList.append(a)

        elif type(a) is int and a % 2 != 0:
            intListodd.append(a)

        #checking for strings
        else:
            strList.append(a)
        
             
    return {"evens": intList,"odds": intListodd,"chars": strList}

print(list_sort([1,2,3,4,5,6,'a','b','c']))
   
