# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import copy

#make dict
#read dict when call function
#io.imread(path + map)
        
def read_image(image):
    try: 
        img = io.imread('./data/' + image)
        return img
    except:
        print('image file name invalid')

#upper = 100, lower = 50
def find_red_pixels(map_filename = 'map.png', upper_threshold = 100, lower_threshold = 50):
    """
    description of function: from specified map file and thresholds for color values,
    creates jpg file with white pixels on black background in place of all red pixels in original image
    param: map_filename - name of image file to find red pixels in
    param: upper_threshold - upper color value to evaluate red color
    param: lower_threshold - lower color value to evaluate red color
    return: none - simply ends function by storing a new jpg file with white pixels instead of red from original on black background
    """

    # Your code goes here
    #intiialize variables
    img = read_image(map_filename)
    upper_lim = upper_threshold
    lower_lim = lower_threshold
    #create empty array in shape of image
    redmap = np.zeros([img.shape[0],img.shape[1]], dtype=float)
    #for every pixel in image shape
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            #simplify color variables into parts of image
            r = img[row][col][0]
            g = img[row][col][1]
            b = img[row][col][2]
            #if red > upper, and green & blue < lower
            if r > upper_lim and g < lower_lim and b < lower_lim:
                #fill pixel in empty array with white where red was
                redmap[row][col] = 1
    #save now filled array as new jpg image
    io.imsave('./data/map-red-pixels.jpg', redmap)

#upper = 100, lower = 50
def find_cyan_pixels(map_filename = 'map.png', upper_threshold = 100, lower_threshold = 50):
    """
    description of function: from specified map file and thresholds for color values,
    creates jpg file with white pixels on black background in place of all cyan pixels in original image
    param: map_filename - name of image file to find cyan pixels in
    param: upper_threshold - upper color value to evaluate cyan color
    param: lower_threshold - lower color value to evaluate cyan color
    return: none - simply ends function by storing a new jpg file with white pixels instead of cyan from original on black background
    """

    # Your code goes here
    #intiialize variables
    img = read_image(map_filename)
    upper_lim = upper_threshold
    lower_lim = lower_threshold
    #create empty array in shape of image
    cyanmap = np.zeros([img.shape[0],img.shape[1]], dtype=float)
    #for every pixel in image shape
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            #simplify color variables into parts of image
            r = img[row][col][0]
            g = img[row][col][1]
            b = img[row][col][2]
            #if red < lower, and green & blue > upper
            if r < lower_lim and g > upper_lim and b > upper_lim:
                #fill pixel in empty array with white where cyan was
                cyanmap[row][col] = 1
    #save now filled array as new jpg image
    io.imsave('./data/map-cyan-pixels.jpg', cyanmap)

def detect_connected_components(IMG):
    """
    description of function: from specified map file, creates 2D array MARK and writes number of pixels inside each connected component region into a text file
    and finds connected components in image
    param: IMG - image file name
    return: MARK and cc-output-2a.txt - 2D array and text file containing connected component pixels
    """

    # Your code goes here
    pavement = 250
    img = read_image(IMG)
    MARK = np.zeros([img.shape[0],img.shape[1]], dtype=int) #set elems as unvisited
    Q = np.array([])
    #iterate through every pixel in image:
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            color = img[x,y]
            #if pixel is pavement and MARK is unvisited:
            if color >= pavement and MARK[x,y] == 0: 
                Q = np.append(Q, [x, y]) #add pixel to Q
                MARK[x,y] = 1 #set MARK to visited
                #While Q is not empty:
                while np.size(Q) > 0: 
                    firstelem = int(Q[0]) #store first element q(m,n)
                    Q = Q[1:] #remove first element from Q
                    #for each 8-neighbor of q(m, n)
                    for s in range(firstelem-1, firstelem+2):
                        for t in range(firstelem-1, firstelem+2):
                            try: #ensure pixel can be checked
                                #if n(s,t) is pavement and MARK(s,t) is unvisited:
                                if img[s,t] == 1 and MARK[s,t] == 0:
                                    MARK[s,t] = 1 #set MARK as visited
                                    Q = np.append(Q, img[s,t]) #add n(s,t) to Q
                            except IndexError:
                                pass
    #find length of each connected component
    #initialize variables
    count = 0
    cclen = []
    #for each pixel in MARK:
    for row in range(MARK.shape[0]):
        for col in range(MARK.shape[1]):
            #if pixel of MARK is not 0:
            if MARK[row][col] != 0:
                count += 1 #add to counter
        if count > 0:
            cclen.append(count)
            count = 0
    
    #create text file and write to it
    sum = 0
    i = 0
    txtfile = open("cc-output-2a.txt", "w")
    for item in cclen:
        txtfile.write(f'\nConnected Component {i}, number of pixels = {item}')
        i += 1
    txtfile.write(f'\nTotal number of connected components = {i}')

    return MARK

def detect_connected_components_sorted(MARK):
    """
    description of function: from specified map file, creates list of values in MARK, sorts then reverses list,
    and stores on text file
    param: MARK - detect_connect_components(with image file)
    return: cc-output-2b.txt - text file containing all components in decreasing order
    """

    # Your code goes here
    #initialize variables
    count = 0
    cclen = []
    revlist = []
    #for each pixel in MARK:
    for row in range(MARK.shape[0]):
        for col in range(MARK.shape[1]):
            #while pixel of MARK is not 0:
            if MARK[row][col] != 0:
                count += 1 #add to counter
        if count > 0:
            cclen.append(count)
            count = 0
    
    newcclen = copy.deepcopy(cclen)
    #sort list into increasing order using insertion sort algorithm
    for v in range(1, newcclen.__len__()):
        key = newcclen[v]
        j = v
        while j >= 1 and newcclen[j-1] > key:
            newcclen[j] = newcclen[j-1]
            j -= 1
        newcclen[j] = key
    #reverse list
    for i in range(len(newcclen)-1, -1, -1):
        revlist.append(newcclen[i])
    #write all values into text file
    txtfile = open("cc-output-2b.txt", "w")
    for item in revlist:
        txtfile.write(f'\nConnected Component {cclen.index(item)}, number of pixels = {item}')
        i += 1
    txtfile.write(f'\nTotal number of connected components = {i}')