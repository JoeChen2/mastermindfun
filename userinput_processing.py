def processinput(rand):#outputs a list with each element as an interger
    print("enter a string of number",len(rand),"long:",end="")
    userinput = input()
    ok=checktype(userinput) and checklenght(rand,userinput)
    

    
    while (ok==False):#if the input is incorrect format it ask the user for another input
        
        userinput = input()
        ok=checktype(userinput) and checklenght(rand,userinput)

    userinput=stringtolist(userinput)#finally turn it into list
    
    return userinput


def checklenght(rand,userinput):#check if the lenght of string is same as rand
    if len(userinput) != len(rand):
        print("your input needs to be",len(rand),"digits long")
        return False
    else:
        return True

def checktype(userinput):#check the type for each element of userinput to ensure they can be turnt into int
    for x in userinput:
        try:
            int(x)
        except:
            print("\nplease use only numbers in the input")
            return False
    return True



    
def stringtolist(userinput):
    userinput = list(userinput)
    
    for x in range(len(userinput)):#turns each element into interger
        userinput[x] = int(userinput[x])
    return userinput
