code = {
        "A":"T",
        "G":"C",
        "T":"A",
        "C":"G"
        }
import itertools

def foo(l,k):
    yield from itertools.product(*([l]*k))

def genepart(k):
    kmers = []
    for x in foo("ACGT",k):
        kmers.append("".join(x))
    return kmers

def countdistinctkmers(kmers, k):
    for i in kmers:
        oppok = ""
        for letter in i:
            oppok += code[letter]
        reversek = oppok[::-1]
        if reversek !=i:
            kmers.remove(reversek)
    return len(kmers)

def function(k):
    power = k/2
    return (4**k-4**power)/2+(4**power)

totalcounts = []
for k in range(1, 31):
    firstgen = genepart(k)
    blub = countdistinctkmers(firstgen, k)
    totalcounts.append(blub)
    print("Done with %d" %k, flush=True)

for i in range(0, 30):
    thing = i+1
    if totalcounts[i] != function(thing):
        print("oops",flush=True)

