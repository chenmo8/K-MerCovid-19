import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("25mercounts.csv")

print("Reading done", flush=True)

k = 25

dkmersref = 0
dataref = list(data.iloc[4])
for i in dataref:
    if i!=0:
        dkmersref +=1

print("Distinct K-mers Ref. Genome Calculations Done", flush=True)

mutationspergenome = {}
for i in range(0, len(data)):
    if i !=4:
        datfa = list(data.iloc[i])
        lendistinctkmers = 0
        for i in datfa:
            if i!=0:
                lendistinctkmers +=1
        mutate = abs(dkmersref-lendistinctkmers)/k
        mutationspergenome.add(mutate)

print("Mutation Calculations Done", flush=True)

mutates = {} #Dictionary that stores in {#of mutations: #of genomes with that number of mutations
for i in range(0, max(mutationspergenome)):
    gperm = 0
    for z in mutationspergenome:
        if z==i:
            gperm +=1
    mutates.update({i:gperm})

print("Dictionary Done", flush=True)
fig = matplotlib.pyplot.figure(1)
fig.suptitle('Estimated Mutations')
plt.xlabel('Number of Mutations')
plt.ylabel("Number of Genomes")
plt.plot(list(mutates.keys()), list(mutates.values()))
plt.show()

plt.savefig("figuremutations.png")

