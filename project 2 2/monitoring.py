# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification.
# 
# This module will access data from the LondonAir Application Programming Interface (API)
# The API provides access to data to monitoring stations. 
# 
# You can access the API documentation here http://api.erg.ic.ac.uk/AirQuality/help
#

import requests
import datetime
import matplotlib.pyplot as plt

def get_live_data_from_api(site_code='MY1',species_code='NO',start_date=None,end_date=None):
    """
    Return data from the LondonAir API using its AirQuality API. 
    
    *** This function is provided as an example of how to retrieve data from the API. ***
    It requires the `requests` library which needs to be installed. 
    In order to use this function you first have to install the `requests` library.
    This code is provided as-is. 
    """
    import requests
    import datetime
    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    
    
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
   
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )

    res = requests.get(url)
    return res.json()


def print_formatted_data(site_code='MY1', species_code='NO',start_date=None,end_date=None):
    """
    description of function: from specified site & species code, and start & end dates,
    print available real-time data in organized format
    param: site_code - code of monitoring station
    param: species_code - code of pollutant
    param: start_date - first date to grab data from
    param: end_date - where to end data
    return: none - no return, just print data as it is received
    """
    # Your code goes here
    #store live data from function above in variable for iteration
    data = get_live_data_from_api(site_code, species_code,start_date,end_date)
    #iterate through keys and values in dictionary found in 'Data' section
    for line in data['RawAQData']['Data']:
        for k, v in line.items():
            print(k.replace('@','') + ' : ' + v) #print keys and values
        print('')


def create_value_list(site_code='MY1', species_code='NO',start_date=None,end_date=None):
    """
    description of function: from specified site & species code, and start & end dates,
    create a list containing only values at each hour as data becomes available if the value contains data
    param: site_code - code of monitoring station
    param: species_code - code of pollutant
    param: start_date - first date to grab data from
    param: end_date - where to end data printing from
    return: value_list - list containing all value data without missing data
    """
    # Your code goes here
    #initialize list
    value_list = []
    #retrieve data from api using function
    data = get_live_data_from_api(site_code, species_code,start_date,end_date)
    #iterate through each line in the dictionary created
    for line in data['RawAQData']['Data']:
        for k, v in line.items(): #for every key and element
            linestr = k.replace('@','') + ' : ' + v #remove @ symbols
            #if the first index shows the string is a value and the length is long enough to contain data
            if linestr[0] == 'V' and len(linestr) > 8: 
                value_list.append(linestr) #append to final list

    return value_list #return list


def find_calculations(site_code='MY1', species_code='NO',start_date=None,end_date=None):
    """
    description of function: from specified site & species code, and start & end dates,
    sort list into increasing order and print the list, median value, and index it was found at as well as average
    param: site_code - code of monitoring station
    param: species_code - code of pollutant
    param: start_date - first date to grab data from
    param: end_date - where to end data
    return: none - no return but prints formatted median value and its index
    """

    # Your code goes here
    #initialize variables
    value_list = create_value_list(site_code, species_code, start_date, end_date)
    sum = 0
    avg = 0
    #sort list into increasing order using bubble sort
    while True:
        swapped = False
        for i in range (len (value_list) -1):
            if value_list[i] > value_list[i +1]:
                value_list[i+1] , value_list[i] = value_list[i], value_list[i+1]
                swapped = True
        if not swapped :
            break
    l = len(value_list)
    print(value_list)
    for value in value_list:
        sum += float(value[7:])
    avg = sum/l
    #find middle value based on length of list
    if l%2 != 0:
        med = float(value_list[l//2][7:]) #if length is even, find index in middle
        medindex = value_list.index(value_list[l//2])
        print(f'Median: {med}   Median Index: {medindex}   Average: {round(avg,1)}')
    else: #if length is odd, find average of two middle values
        med1 = float(value_list[l//2][7:])
        med2 = float(value_list[l//2 - 1][7:])
        med = float(med1 + med2)/2
        medindex1 = value_list.index(value_list[l//2])
        medindex2 = value_list.index(value_list[l//2 - 1])
        #print formatted calculations
        print(f'Median: {med}   Median Index between: {medindex2} and: {medindex1}    Average: {round(avg,1)}')
    
    
def graphdata(site_code='MY1', species_code='NO',start_date=None,end_date=None):
    """
    description of function: from specified site & species code, and start & end dates,
    graph datapoints at each hour
    param: site_code - code of monitoring station
    param: species_code - code of pollutant
    param: start_date - first date to grab data from
    param: end_date - where to end data
    return: none - no return but displays graph containing data at each hour
    """
    # Your code goes 
    #initialize variables
    data = get_live_data_from_api(site_code='MY1', species_code='NO',start_date=None,end_date=None)
    l1 = []
    l2 = []
    datestr = ''
    #iterate through keys and values in dictionary found in 'Data' section
    for line in data['RawAQData']['Data']:
        for k, v in line.items():
            if k[1] == 'M': #if key is the Date:
                timesplit = v.split(' ')
                datestr = timesplit[1][:5]
                l1.append(datestr) #append hour to list
            elif k[1] == 'V' and len(v) > 0: #if key is Value:
                valstr = float(v) #append numerical value
                l2.append(valstr) #append value to list
            while len(l1) > len(l2): #allign list lengths for plotting
                l1.pop(-1)
    #plot datapoints onto graph and display it
    plt.plot(l1, l2)
    plt.show()