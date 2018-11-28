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
        elif type(a) is str:
            strList.append(a)
        
             
    return {"Even": intList,"odd": intListodd,"character": strList}

print(list_sort([2,0,6,5,1,7,'z','a']))
   
