import csv
import os
import numpy
import pandas as pd

directory = r"/home/connieh/Desktop/K-MerCovid-19"
  
totalkers = {}

k = 0

indexes = []

numpytry = []

for filename in os.listdir(directory):
    kmersforthatfile = []
    if filename.endswith(".fa"):
        _file = open(filename, "r")
        content = _file.read()
        splitcon = content.split(">")
        for i in splitcon[1:len(splitcon)]:
            twtwo = i.split()
            kmersforthatfile.append(twtwo[1])
        indexes.append(k)
        k +=1
        if k%2 !=0:
            fourtok = (4**k)/2
        else:
            fourtok = (4**k)
        estim = 30265-k+1
        numpytry.append([k, len(kmersforthatfile),fourtok,estim])
        totalkers.update({k:len(kmersforthatfile)})
    else:
        continue

a = numpy.asarray(numpytry)
numpy.savetxt("foo.csv", a, delimiter=",")
