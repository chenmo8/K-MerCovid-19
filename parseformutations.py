#This code finds the average mutation per genome based on ALL the reads. (Not Individually)
#Part 1, Find number B

k = 25

buniquekmers = open("dump25mercounts.fa", "r")
bunique = buniquekmers.read()
splitbunique = bunique.split(">")

totalbkmers = []

for i in splitbunique[1:len(splitbunique)]:
    twtwo = i.split()
    totalbkmers.append(twtwo[1])

totalbkmerslength = len(splitbunique)

#Part 2, find number A

auniquekmers = open("25mersall.fa", "r")
aunique = auniquekmers.read()
splitaunique = aunique.split(">")

totalakmers = []

totalakmerslength = len(splitaunique)

for i in splitaunique[1:len(splitaunique)]:
    twtwo = i.split()
    totalakmers.append(twtwo[1])

kmersbymutations = totalakmerslength-totalbkmerslength
distinctmutations = kmersbymutations/k
averagemutationpergenome = distinctmutations/3970
print(averagemutationpergenome)
print(distinctmutations)
