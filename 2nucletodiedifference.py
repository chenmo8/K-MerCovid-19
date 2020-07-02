import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("25mercounts.csv")

print("Reading done")

dkmersref = len(data.columns())-2

mutationspergenome = {}
for row in data:
    datfa = list(data.iloc[row[0]])
    lendistinctkmers = 0
    for i in datfa:
        if i!=0:
            lendistinctkmers +=1
    mutate = abs(dkmersref-lendistinctkmers)/k
    mutationspergenome.add(mutate)

mutates = {} #Dictionary that stores in {#of mutations: #of genomes with that number of mutations
for i in range(0, max(mutationspergenome)):
    mutates.update({i:len(i in mutationspergenome)})

fig = matplotlib.pyplot.figure(1)
fig.suptitle('Estimated Mutations')
plt.xlabel('Number of Mutations')
plt.ylabel("Number of Genomes")
plt.plot(list(mutates.keys()), list(mutates.values()))
plt.show()

