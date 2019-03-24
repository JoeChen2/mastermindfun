#function called Compare to compare the users guess to the random number
#checks if number and position are correct
#checks if number is correct but out of position
#inputs   R: random number
#         U: user number
#outputs CP: number of values with correct value and position
#        CN: number of values with correct value

def Compare(R,U):

    CP = 0
    CN = 0

    #get length of each set of values. same for both so R used.
    L = len(R)

    #check if value and position of each value are the same
    i = 0
    while i < L:
        
        if R[i] == U[i]:
            CP += 1

    #check if values are correct but out of position            
        elif U[i] in R:
            CN += 1  
        i += 1

    return CP, CN

#####test
##a=[2,2,2,2]
##b=[2,1,1,1]
##c=[1,1,1,2]
##
##
##print(Compare(a,b))
##print(Compare(b,a))
##print(Compare(a,c))
##print(Compare(c,a))




