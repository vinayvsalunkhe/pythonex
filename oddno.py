#To display odd number in the given numerical integer string

pylist=[1,2,3,4,5,6,7,8,9]
print('the odd numbers in the given list are:',pylist)
for i in range(0,9,1):
    if(pylist[i]%2!=0):
        print(pylist[i])
        
