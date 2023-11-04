def max_num(inputArr):
    if(len(inputArr)!=3):
        print(f'enter an array of length 3')
        return "error"
    
    maxValue = max(inputArr)
    print("The max value of the list provided is: ", maxValue)

    return maxValue

def mult_list(inputArr):
    result = 1
    for item in inputArr:
        result *= item

    print(f"the result of multiplying each item in the array is: ", result)
    return result

max_num([1,2,3])
mult_list([1,2,3])