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

def rev_string(str):
    result = str[::-1]
    print(f"the original string is: ", str, " and reversed: ", result.capitalize())
    return result


def num_within(test,first,last):
    if(test > first and test < last):
        print(f'The test value ',test,' is within the range of', first, ' and ', last)
        result = True
    else: 
        print(f'The test value ',test,' is not within the range of ', first, ' and ', last)
        result = False
    return result



def pascal(val):
    for item in range(val):
        print(' '*(val-1), end='')
        print(' '.join(map(str,str(11**item))))

max_num([1,2,3])
mult_list([1,2,3])
rev_string("Duck")
num_within(3,2,4)
num_within(10,2,5)
pascal(5)