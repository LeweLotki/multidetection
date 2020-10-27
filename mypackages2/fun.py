import cv2 
import numpy as np 
import random

def detection(list, array):
    temp = []
    for val in list:
        if array[val[0],val[1],0] < 50 and array[val[0],val[1],1] < 50 and array[val[0],val[1],2] > 220:
            temp.extend([[val[0],val[1]]])
    list.clear()
    list.extend(temp)
    
def resultant(list):
    result = 0 
    all_x = 0
    all_y = 0
    lenght = len(list)
    if lenght == 1:
        result = list[0]
    elif lenght > 1:
        for val in list:
            all_x += val[0]
            all_y += val[1]
        all_x = int(all_x/lenght)
        all_y = int(all_y/lenght)
        result = [all_x,all_y]
    if type(result) == int:
        print(result)
    return result
    
def radiation(num,list1):
    radiation = 0
    temp = distance(num, list1)
    for val in temp:
        if val[1] > radiation:
            radiation = val[1]
    return radiation

def distance(num, list):
    temp = []
    temp2 = []
    for val in list:
        d = int(((num[0]-val[0])**2 + (num[1]-val[1])**2)**0.5)
        temp.append(d)
    for i in range(0, len(list)):
        temp2.extend([[list[i],temp[i]]])
    return temp2

def average(list):
    sum = 0
    for val in list: 
        sum += val[1]
    sum = int(sum/len(list))
    return sum
    
def deviation(list, num):
    sum = 0
    for val in list:
        sum += (val[1] - num)**2
    sum = sum/len(list)
    sum = int((sum)**0.5)
    return sum
    
def unify(dist, dev, points):
    a = 0
    b = dev
    i = 0
    density = False
    temp = []
    density = True
    while density:
        for val in dist:
            if val[1] in range(a, b):
                temp.extend([val[0]])
                if val[0] in points:
                    points.remove(val[0])
            else:
                i += 1
                if i == len(dist):
                    density = False
                    break             
        a += int(dev/2)
        b += int(dev/2)
        i = 0
    if len(temp) == 0:
        print('ERROR')
    return temp
        
    