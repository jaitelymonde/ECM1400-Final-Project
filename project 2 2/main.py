# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

from reporting import datadictionary, daily_average, daily_median, hourly_average, monthly_average, peak_hour_date, count_missing_data, fill_missing_data
from intelligence import read_image, find_red_pixels, find_cyan_pixels, detect_connected_components, detect_connected_components_sorted
from monitoring import get_live_data_from_api, create_value_list, print_formatted_data, graphdata, find_calculations

def main_menu():
    """
    description of function: creates main user interface to navigate through modules/their functions
    param: no parameters
    return: no return
    """
    # Your code goes here
    print('\nMAIN MENU') #title
    #choices
    print('\nR - Access the PR module')
    print('I - Access the MI module')
    print('M - Access the RM module')
    print('A - Print the About text')
    print('Q - Quit the application')
    choice = str(input('Enter module choice: '))
    print()
    while choice != 'Q':
        if choice == 'R':
            reporting_menu()
        elif choice == 'I':
            intelligence_menu()
        elif choice == 'M':
            monitoring_menu()
        elif choice == 'A':
            about()
        else:
            print('\nNot an option')
            main_menu()
        print('')
        main_menu()
    print('Application quit.')
    quit()

def reporting_menu():
    """
    description of function: displays menu to select amongst reporting functions
    and allows user to enter in values for function
    param: no parameters
    return: no return
    """
    # Your code goes here 

    #choices
    print('\nEntered PR module.')
    print('\nDA - Find daily average')
    print('DM - Find daily median')
    print('HA - Find hourly average')
    print('MA - Find monthly average')
    print('PHD - Find peak hour date')
    print('CMD - Count missing data')
    print('FMD - Fill missing data')
    print('H - Return to main menu')
    choice = str(input('Enter function choice: ')) #storing choice as input
    #choosing function and creating inputs based on choice, trying function to see if arguments correct
    if choice == 'DA':
        station = str(input('Enter station name (Harlington, Marylebone, or Kensington): '))
        pollutant = str(input('Enter pollutant (no, pm10, or pm25): '))
        try:
            print(daily_average(datadictionary(), station, pollutant))
        except:
            print('Invalid argument(s), returning to reporting menu')
    if choice == 'DM':
        station = str(input('Enter station name (Harlington, Marylebone, or Kensington): '))
        pollutant = str(input('Enter pollutant (no, pm10, or pm25): '))
        try:
            print(daily_median(datadictionary(), station, pollutant))
        except:
            print('Invalid argument(s), returning to reporting menu')
    if choice == 'HA':
        station = str(input('Enter station name (Harlington, Marylebone, or Kensington): '))
        pollutant = str(input('Enter pollutant (no, pm10, or pm25): '))
        try:
            print(hourly_average(datadictionary(), station, pollutant))
        except:
            print('Invalid argument(s), returning to reporting menu')
    if choice == 'MA':
        station = str(input('Enter station name (Harlington, Marylebone, or Kensington): '))
        pollutant = str(input('Enter pollutant (no, pm10, or pm25): '))
        try:
            print(monthly_average(datadictionary(), station, pollutant))
        except:
            print('Invalid argument(s), returning to reporting menu')
    if choice == 'PHD':
        date = str(input('Enter date (e.g. 2021-01-9): '))
        station = str(input('Enter station name (Harlington, Marylebone, or Kensington): '))
        pollutant = str(input('Enter pollutant (no, pm10, or pm25): '))
        try:
            print(peak_hour_date(datadictionary(), date, station, pollutant))
        except:
            print('Invalid argument(s), returning to reporting menu')
    if choice == 'CMD':
        station = str(input('Enter station name (Harlington, Marylebone, or Kensington): '))
        pollutant = str(input('Enter pollutant (no, pm10, or pm25): '))
        try:
            print(count_missing_data(datadictionary(), station, pollutant))
        except:
            print('Invalid argument(s), returning to reporting menu')
    if choice == 'FMD':
        newval = str(input('Enter new value to be replaced: '))
        station = str(input('Enter station name (Harlington, Marylebone, or Kensington): '))
        pollutant = str(input('Enter pollutant (no, pm10, or pm25): '))
        try:
            print(fill_missing_data(datadictionary(), newval, station, pollutant))
        except:
            print('Invalid argument(s), returning to reporting menu')
    if choice == 'H':
        print('returning to main menu')
        main_menu()
    else:
        reporting_menu()


def monitoring_menu():
    """
    description of function: displays menu to select amongst monitoring functions
    and allows user to enter in values for function
    param: no parameters
    return: no return
    """

    # Your code goes here
    print('\nEntered RM module.')
    print('\nVL - Create value list')
    print('PD - Print data formatted')
    print('FC - Find calculations of median, its index, and average')
    print('CG - Create graph')
    print('H - Return to main menu')
    choice = str(input('Enter function choice: ')) #storing choice as input
    if choice == 'VL':
        site = str(input('Enter site code: '))
        species = str(input('Enter species code: '))
        start = str(input('Enter start date: '))
        end = str(input('Enter start date: '))
        create_value_list(site, species, start, end)
    if choice == 'PD':
        site = str(input('Enter site code: '))
        species = str(input('Enter species code: '))
        start = str(input('Enter start date: '))
        end = str(input('Enter end date: '))
        print_formatted_data(site, species, start, end)
    if choice == 'FC':
        site = str(input('Enter site code: '))
        species = str(input('Enter species code: '))
        start = str(input('Enter start date: '))
        end = str(input('Enter end date: '))
        find_calculations(site, species, start, end)
    if choice == 'CG':
        site = str(input('Enter site code: '))
        species = str(input('Enter species code: '))
        start = str(input('Enter start date: '))
        end = str(input('Enter end date: '))
        graphdata(site, species, start, end)
    if choice == 'H':
        print('returning to main menu')
        main_menu()
    else:
        monitoring_menu()


def intelligence_menu():
    """
    description of function: display intelligence menu for user to select among functions
    param: none
    return: none - no return but displays menu
    """
    # Your code goes here
    print('\nEntered MI module.')
    print('\nFRP - Find red pixels')
    print('FCP - Find cyan pixels')
    print('DC - Detect connect components')
    print('SC - Sort connected components')
    print('H - Return to main menu')
    choice = str(input('\nEnter function choice: ')) #storing choice as input
    #based on choice execute functions with inputs for parameters
    if choice == 'FRP':
        imagefile = str(input('Enter image filename: '))
        upper = str(input('Enter upper threshold: '))
        lower = str(input('Enter lower threshold: '))
        find_red_pixels(imagefile, upper, lower)
        print('image stored')
    if choice == 'FCP':
        imagefile = str(input('Enter image filename: '))
        upper = str(input('Enter upper threshold: '))
        lower = str(input('Enter lower threshold: '))
        find_cyan_pixels(imagefile, upper, lower)
        print('image stored')
    if choice == 'DC':
        imagefile = str(input('Enter image filename: '))
        detect_connected_components(imagefile)
    if choice == 'FC':
        imagefile = str(input('Enter image filename: '))
        detect_connected_components_sorted(detect_connected_components(imagefile))
    if choice == 'H':
        print('Returning to main menu')
        main_menu()
    else:
        intelligence_menu()

def about():
    """
    description of function: print string with module code and candidate number, and return to main menu
    param: site_code - code of monitoring station
    param: species_code - code of pollutant
    param: start_date - first date to grab data from
    param: end_date - where to end data
    return: none - no return but displays graph containing data at each hour
    """

    # Your code goes here
    print('\nDisplaying \'About\' text.')
    print('\n(ECM1400) 238737')
    main_menu()

def quit():
    """
    description of function: quit program
    param: none
    return: none
    """
    # Your code goes here
    exit()


if __name__ == '__main__':
    main_menu()