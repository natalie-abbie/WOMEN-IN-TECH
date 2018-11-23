def fizzbuzz(x,y):
#divisable by 3 and 5 and returns a reminder 0
    
    if (x+y)%3 == 0 and (x+y)%5 == 0:
        print('fizzbuzz')
#divisiable by 5 and returns reminder 0
    
    elif (x+y)%5 == 0:
        print('buzz')
#divisiable by 3 and returns reminder 0
    
    elif (x+y)%3 == 0:
        print('fizz')

    else:
        print(x+y)
        
#input the numbers to be divided by 3 or 5 
fizzbuzz(x,y)
