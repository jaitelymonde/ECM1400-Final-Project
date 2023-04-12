# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

import numpy as np
import copy


def datadictionary():
    path = './data/'
    harl_dict = {'date': [], 'time': [], 'no': [], 'pm10': [], 'pm25': []}
    mary_dict = {'date': [], 'time': [], 'no': [], 'pm10': [], 'pm25': []}
    nken_dict = {'date': [], 'time': [], 'no': [], 'pm10': [], 'pm25': []}

    with open(path + 'Pollution-London Harlington.csv', 'r') as f:
            a = f.readlines()
            for line in a:
                x = line.split(',')
                harl_dict['date'].extend([x[0].strip()])
                harl_dict['time'].extend([x[1].strip()])
                harl_dict['no'].extend([x[2].strip()])
                harl_dict['pm10'].extend([x[3].strip()])
                harl_dict['pm25'].extend([x[4].strip()])

    with open(path + 'Pollution-London Marylebone Road.csv', 'r') as f:
            a = f.readlines()
            for line in a:
                x = line.split(',')
                mary_dict['date'].extend([x[0].strip()])
                mary_dict['time'].extend([x[1].strip()])
                mary_dict['no'].extend([x[2].strip()])
                mary_dict['pm10'].extend([x[3].strip()])
                mary_dict['pm25'].extend([x[4].strip()])

    with open(path + 'Pollution-London N Kensington.csv', 'r') as f:
            a = f.readlines()
            for line in a:
                x = line.split(',')
                nken_dict['date'].extend([x[0].strip()])
                nken_dict['time'].extend([x[1].strip()])
                nken_dict['no'].extend([x[2].strip()])
                nken_dict['pm10'].extend([x[3].strip()])
                nken_dict['pm25'].extend([x[4].strip()])

    data_dict = {'Harlington': {'date': [], 'time': [], 'no': [], 'pm10': [], 'pm25': []}, 'Marylebone': {'date': [], 'time': [], 'no': [], 'pm10': [], 'pm25': []}, 'Kensington': {'date': [], 'time': [], 'no': [], 'pm10': [], 'pm25': []}}
    for key in harl_dict:
        data_dict['Harlington'][key].extend(harl_dict[key])
    for key in mary_dict:
        data_dict['Marylebone'][key].extend(mary_dict[key])
    for key in nken_dict:
        data_dict['Kensington'][key].extend(nken_dict[key])

    return data_dict

def daily_average(data, monitoring_station:str, pollutant:str):
    """
    description of function: from specified monitoring station and pollutant in data,
    find average of each day and stores in list
    param: data - data file containing pollution data
    param: monitoring_station - specified station that data is grabbing from
    param: pollutant - pollutant to grab data from within monitoring station
    return: avgperday - list containing 365 values of average data (one for each day)
    """
    
    ## Your code goes here
    #initialize variables
    avgperday = []
    totalday = []
    sum = 0.0
    avg = 0.0
    count = 0
    i = 0
    #if pollutant string is present in data, remove it
    if pollutant in data[monitoring_station][pollutant]:
        data[monitoring_station][pollutant].remove(pollutant)
    #for every value in dataset append float to new list if value is numeric, 0 if 'No data'
    for val in data[monitoring_station][pollutant]:
        if val[0].isnumeric():
            totalday.append(float(val))
        else:
            totalday.append(0)
        totalarr = np.array(totalday) #create numpy array from list of numerical stored data
    #iterate through array in sets of 24 to find sum of each day
    while i < totalarr.__len__(): 
        for val1 in totalarr[i:i+24]:
            if val1 != 0:
                sum += val1 
            else:
                count += 1
        i += 24 #change i for next set of 24 hours
        avg = sum/(24-count) #calculate average, subtract denominator 24 by each point of missing data
        sum = 0 #reset sum and count for next set of 24 hours
        count = 0 
        avgperday.append(avg) #append average to avgperday list
    return avgperday #return final list of 365 averages (1 per day)

def daily_median(data, monitoring_station:str, pollutant:str):
    """
    description of function: from specified monitoring station and pollutant in data,
    finds median of each day and stores in list
    param: data - data file containing pollution data
    param: monitoring_station - specified station that data is grabbing from
    param: pollutant - pollutant to grab data from within monitoring station
    return: medianperday - list containing 365 values of mean data (one for each day)
    """

    ## Your code goes here
    #initialize variables
    day = []
    totalday = []
    medianperday = []
    i = 0
    #if pollutant string is present in dataset, remove it
    if pollutant in data[monitoring_station][pollutant]:
        data[monitoring_station][pollutant].remove(pollutant)
    #for every value in dataset append float to new list if value is numeric, 0 if 'No data'
    for val in data[monitoring_station][pollutant]:
        if val[0].isnumeric():
            totalday.append(float(val))
        else:
            totalday.append(0)
        totalarr = np.array(totalday) #create numpy array from numerical stored data
    #iterate through array in sets of 24 and append to a 'day' list
    while i < totalarr.__len__(): 
        for val1 in totalarr[i:i+24]:
            day.append(val1)
        i += 24
        list(filter((0).__ne__, day)) #filter out 0s ('No data' points)
        #sort day list into increasing order using insertion sort algorithm
        for v in range(1, day.__len__()):
            key = day[v]
            j = v
            while j >= 1 and day[j-1] > key:
                day[j] = day[j-1]
                j -= 1
            day[j] = key
        l = day.__len__()
        #find middle value based on length of list
        if l%2 != 0: 
            med = day[l//2] #if length is even, find index in middle
        else: #if length is odd, find average of two middle values
            med1 = day[l//2]
            med2 = day[l//2 - 1]
            med = (med1 + med2)/2
        medianperday.append(med) #append to medianperday list 
    return medianperday #return final list of 365 median values (one for each day)


def hourly_average(data, monitoring_station:str, pollutant:str):
    """
    description of function: from specified monitoring station and pollutant,
    finds the average of each hour 1:00 - 24:00 and stores in list
    param: data - data file containing pollution data
    param: monitoring_station - specified station that data is grabbing from
    param: pollutant - pollutant to grab data from within monitoring station
    return: avgperhr - list containing 24 average values (one for each hour)
    """
    
    ## Your code goes here
    #initialize variables
    avgperhr = [[] for _ in range(24)]
    totalday = []
    hrlist = [[] for _ in range(24)]
    sum = 0.0
    avg = 0.0
    count = 0
    i = 0
    ind = 0
    #if pollutant string is present in dataset of station and pollutant, remove it
    if pollutant in data[monitoring_station][pollutant]:
        data[monitoring_station][pollutant].remove(pollutant)
    #for every value in dataset append float to new list if value is numeric, 0 if 'No data'
    for val in data[monitoring_station][pollutant]:
        if val[0].isnumeric(): 
            totalday.append(float(val))
        else:
            totalday.append(0)
        totalarr = np.array(totalday) #create numpy array from numerical list
    #iterate through array in sets of 24 to append values to new list at each index for every hour
    while i < totalarr.__len__(): 
        for val1 in totalarr[i:i+24]: 
            if val1 != 0: 
                hrlist[ind].append(val1) 
                ind +=1 
            else: 
                hrlist[ind].append(0)
                ind += 1
        #reset index values for next set of 24
        ind = 0 
        i += 24
        
    ind = 0
    #sort through list with stored data at each hour of day (24 lists nested)
    while ind < 24:
        for val2 in hrlist[ind]: #for every val at each hour index
            if val2 != 0: #if value is a real datapoint
                sum += val2 #add value to sum
            else:
                count += 1 #else, add 1 to count
        #calculate average of each set of 24 
        avg = sum/(365-count)
        sum = 0
        count = 0
        #append average to avgperhr list at each index 
        avgperhr[ind].append(avg)
        ind += 1
    return avgperhr #return final list with 24 averages (one for each hour of day)

def monthly_average(data, monitoring_station:str, pollutant:str):
    """
    description of function: from specified monitoring station and pollutant in data,
    finds average of each month and stores in list
    param: data - data file containing pollution data
    param: monitoring_station - specified station that data is grabbing from
    param: pollutant - pollutant to grab data from within monitoring station
    return: month_avgs - list containing 12 values of average data (one for each month)
    """
    
    ## Your code goes here
    #initialize variables
    month_avgs = [[] for _ in range(12)]
    totalday = []
    month_data = [[] for _ in range(12)]
    sum = 0.0
    avg = 0.0
    count = 0
    i = 0
    ind = 0
    m = 1
    end = 744
    beg = 744
    #if pollutant string is in dataset from station and pollutant, remove it
    if pollutant in data[monitoring_station][pollutant]:
        data[monitoring_station][pollutant].remove(pollutant)
    #for every value in dataset append float to new list if value is numeric, 0 if 'No data'
    for val in data[monitoring_station][pollutant]:
        if val[0].isnumeric():
            totalday.append(float(val))
        else:
            totalday.append(0)
        totalarr = np.array(totalday) #create numpy array from numerical list
    #iterate through entire array and append to index of new list 'month_data'
    while i < totalarr.__len__():
        for val1 in totalarr[i:end]:
            if val1 != 0:
                month_data[ind].append(val1) #append to index within 12
            else:
                month_data[ind].append(0) #else, append 0 for missing data
        if(ind < 11): #add 1 to index to stay within 12
            ind += 1
        if i < totalarr.__len__(): #if index is less than length of array
            i += beg #add beginning value to i
        m += 1 #add 1 to m, representing the next month
        #alter the value of beginning and end ints for each length of month
        if m == 2:
            beg = 672
            end += 672
        elif m in (4, 6, 9, 11):
            beg = 720
            end += 720
        elif m in(3, 5, 7, 8, 10, 12):
            beg = 744
            end += 744
    ind = 0 #reset index
    #loop through sets of 12 in month_data list to find sum of each month
    while ind < 12: 
        for val2 in month_data[ind]:
            if val2 != 0:
                sum += val2
            else:
                count += 1 #add 1 to count for each point of missing data
        #calcualate average, subtracting count from length for real length
        avg = sum/(month_data[ind].__len__()-count)
        sum = 0
        count = 0
        month_avgs[ind].append(avg) #append average to each index of final average list
        ind += 1
    return month_avgs #return final list of 12 averages (one for each month)


def peak_hour_date(data, date, monitoring_station:str,pollutant:str):
    """
    description of function: from specified monitoring station, date, and pollutant in data,
    finds the hour of that date with the highest number 
    param: data - data file containing pollution data
    param: date - date (e.g. 2021-12-01) pollution data was found
    param: monitoring_station - specified station that data is grabbing from
    param: pollutant - pollutant to grab data from within monitoring station
    return: f'{maxindex + 1}:00', max - index of max number found formatted into hour of day and the max number itself
    """
    
    ## Your code goes here
    #initialize variables
    totalday = []
    dayindex = list(data[monitoring_station]['date']).index(date) - 1
    hrlist = []
    max = 0.0
    #if pollutant string is in dataset from station and pollutant, remove it
    if pollutant in data[monitoring_station][pollutant]:
        data[monitoring_station][pollutant].remove(pollutant)
    #for every value in dataset append float to new list if value is numeric, 0 if 'No data'
    for val in data[monitoring_station][pollutant]:
        if val[0].isnumeric():
            totalday.append(float(val))
        else:
            totalday.append(0)
        totalarr = np.array(totalday) #create numpy array from numerical list
    #iterate through values in array in sets of 24 to create new list of data
    for val1 in totalarr[dayindex:dayindex+24]:
        if val1 != 0:
            hrlist.append(val1)
        else:
            hrlist.append(0)
    #iterate through every value in new list to find maximum value within 1 day
    for val2 in hrlist:
            if val2 > max:
                max = val2
    maxindex = list(hrlist).index(max) #find index of max value
    
    return f'{maxindex + 1}:00', max #return max index and max value formatted to include hour of day


def count_missing_data(data,  monitoring_station:str,pollutant:str):
    """
    description of function: from specified monitoring station and pollutant in data,
    finds each instance of 'No data' and adds to counter 
    param: data - data file containing pollution data
    param: date - date (e.g. 2021-12-01) pollution data was found
    param: monitoring_station - specified station that data is grabbing from
    param: pollutant - pollutant to grab data from within monitoring station
    return: count - total number of instances of 'No data' in data
    """
    
    ## Your code goes here
    #initialize variables
    totalday = []
    count = 0
    #if pollutant string is in dataset from station and pollutant, remove it
    if pollutant in data[monitoring_station][pollutant]:
        data[monitoring_station][pollutant].remove(pollutant)
    #for every value in dataset append float to new list if value is numeric, 0 if 'No data'
    for val in data[monitoring_station][pollutant]:
        if val[0].isnumeric():
            totalday.append(float(val))
        else:
            totalday.append(0)
        totalarr = np.array(totalday) #create numpy array from numerical list
    #iterate through array and count occurences of 0 for missing data ('No data')
    for val1 in totalarr:
            if val1 == 0:
                count += 1
    
    return count #return count of each missing data


def fill_missing_data(data, new_value,  monitoring_station,pollutant):
    """
    description of function: from specified monitoring station and pollutant in data,
    finds each instance of 'No data' and fills it with a new value
    param: data - data file containing pollution data
    param: new_value - input value to replace 'No data' with
    param: date - date (e.g. 2021-12-01) pollution data was found
    param: monitoring_station - specified station that data is grabbing from
    param: pollutant - pollutant to grab data from within monitoring station
    return: new_data - data set of monitoring station returned back updated
    with new values in place of 'No data'
    """
    
    ## Your code goes here
    #if pollutant string is in dataset from station and pollutant, remove it
    if pollutant in data[monitoring_station][pollutant]:
        data[monitoring_station][pollutant].remove(pollutant)
    new_data = copy.deepcopy(data) #create deep copy of dataset
    #iterate through every value in copy to replace missing data with new_value
    for val in new_data[monitoring_station][pollutant]:
        if val == 'No data': #if value has no data
            val_index = list(new_data[monitoring_station][pollutant]).index(val) #find index of 'No data'
            if isinstance(new_value, str): #if new_value is a string append the value itself
                new_data[monitoring_station][pollutant][val_index] = new_value
            else: #else, append string of float to keep data consistent
                new_data[monitoring_station][pollutant][val_index] = str(new_value)
    
    return new_data #return new dataset