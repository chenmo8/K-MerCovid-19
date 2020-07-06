import os
import csv

k= 25

directory = r"/home/connieh/Desktop/25mermutations"

'''
for filename in os.listdir(directory):
    store = []
    if filename.endswith(".fasta"):
        os.system("jellyfish count -m %d -s 100M -t 10 -o %dmertrial%s.jf -C %s" %(k, k, filename, filename))
'''
for filename in os.listdir(directory):
    if filename.endswith("fasta.jf"):
        os.system('jellyfish dump %s > %dmertrial%s.fa' %(filename, k, filename))
