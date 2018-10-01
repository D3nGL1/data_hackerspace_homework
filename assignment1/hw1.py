#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np
import re

def histogram_times(filename):
    with open(filename,encoding = "utf-8") as f:
        csv_reader = csv.reader(f)
        airplane_data = list(csv_reader)
    crash_each_day = [0] * 24
    for incident in airplane_data[1:]:
        if incident[1]:
            time = re.sub('[^0123456789:]+' ,'',incident[1])
            if len(time.split(':')[0]) != 0:
                time1 = int(time.split(':')[0])
            if time1 < 24:
                crash_each_day[time1] += 1
    return crash_each_day

def weigh_pokemons(filename, weight):
    with open(filename,encoding = "utf-8") as load_f:
        pokemon_jason = json.load(load_f)
    weight_name = [[x["weight"],x["name"]]for x in pokemon_jason["pokemon"]]
    print(weight_name)
    name = []
    for x in weight_name:
        w = float(x[0].split(' ')[0])
        if w == weight:
            name.append(x[1])
    return name

def single_type_candy_count(filename):
    with open(filename,encoding = "utf-8") as load_f:
        pokemon_jason = json.load(load_f)
    singletype_candy = [x["candy"] for x in pokemon_jason["pokemon"] if len(x["type"]) == 1]
    candysum = 0
    for candy in singletype_candy:
        if candy == "None":
            continue
        candysum += 1
    return candysum

def reflections_and_projections(points):
    returnArray = np.zeros(points.shape)
    for i in range(0,points.size/2):
        returnArray[0,i] = (6 - 3 * points[0,i] - points[1,i])/10
        returnArray[1,i] = (18 - 9 * points[0,i] - 3 * points[1,i])/10
    return returnArray
    
def normalize(image):
    max = image.max()
    min = image.min()
    image_toReturn = (255/(max-min))*(image - min)
    return image_toReturn

def sigmoid_normalize(image):
    pass
