import random

def generate_random_nunmber(withrepeats,digits):
    output = []
    
    if digits>6:#if there are more than 6 digits ignore the with repeats
        for x in range(digits):
            output.append(random.randrange(0,6))
        return output
    
    elif withrepeats == False:#no repeats and bellow 6 digits
        a=[0,1,2,3,4,5]
        
        for x in range(digits):
            randi = random.randrange(0,len(a))
            output.append(a.pop(randi))

        return output

    
    else:#with repeats and bellow 6 digits
        for x in range(digits):
            output.append(random.randrange(0,6))
        return output
