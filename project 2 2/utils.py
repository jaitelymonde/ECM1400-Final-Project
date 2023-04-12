# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


def sumvalues(values):
    """
    description of function: iterates through list or array and finds sum of all elements
    param: values - list or array of elements to finds sum of
    return: sum - total of all elements added together
    """  
    ## Your code goes here
    #initialize variable
    sum = 0
    #iterate through every value in list to find sum of all items
    for item in values:
        if not isinstance(item, int) | isinstance(item, float): #if item isn't a number
            raise Exception
        sum += item
    return sum #return sum of all values in list


def maxvalue(values):
    """
    description of function: iterates through list or array and finds
    the maximum value of all elements and then returns index of number
    param: values - list or array of elements to find maximum number from
    return: values.index(max) - index of maximum value in list or array
    """  

    ## Your code goes here
    #initialize variable
    max = 0
    #iterate through every value in list to find maximum value
    for item in values:
        if not isinstance(item, int) | isinstance(item, float): #if item isn't a number
            raise Exception
        #check if value is greater than max, updating max if true
        elif item > max:
            max = item
    return values.index(max) #return index of maxmimum value


def minvalue(values):
    """
    description of function: iterates through list or array and finds minimum value of all elements
    param: values - list or array of elements to find minimum value from
    return: values.index(min) - index of minimum value found
    """  

    ## Your code goes here
    #initialize variable
    min = values[0]
    #iterate through every value in list to find minimum value
    for item in values:
        if not isinstance(item, int) or isinstance(item, float): #if item isn't a number
            raise Exception
        #check if value is less than min, updating min if true
        elif item < min:
            min = item
    return values.index(min) #return index of minimum value

L = [1, 2, 3, '4', 5, 6]
print(minvalue(L))

def meannvalue(values):
    """
    description of function: iterates through list or array and calculates mean value
    from total and length of list
    param: values - list or array of elements to find mean from
    return: mean - average of all elements
    """  

    ## Your code goes here
    #initialize variables
    total = 0
    mean = 0
    #iterate through every value in list to find total
    for item in values:
        if not isinstance(item, int) | isinstance(item, float): #if item isn't a number
            raise Exception
        total += item #add value to total
    mean += (total/len(values)) #calculate average
    return mean #return average


def countvalue(values,x):
    """
    description of function: iterates through list or array finds number
    of occurences of input x
    param: values - list or array of elements to find mean from
    param: x - value to find number of occurences from in list or array
    return: 0 or occurences - 0 if x is not in values or number of occurences
    if it was found 1 or more times
    """  

    ## Your code goes here
    #initialize variable
    occurrences = 0
    #iterate through every item in values to find occurences of x
    for item in values:
        if not isinstance(item, int) or isinstance(item, float): #if item isn't a number
            raise Exception #if value is not numerical raise exception
        elif item == x:
            occurrences += 1 #add 1 to occurences if value is equal to x
        elif x not in values: #else if x is not found in values, return 0
            return 0
    return occurrences #otherwise, return number of occurences
