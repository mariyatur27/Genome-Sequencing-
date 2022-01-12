# Lesson 2
# Function that will read the FASTQ file and parse it

def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline() # We skip the first line because we don't need it
            seq = fh.readline().rstrip() # We store the second line in a variable
            fh.readline() # We skip the third line because we don't need it
            qual = fh.readline().rstrip() # We store the fourth line in a variable
            if len(seq) == 0: # Checking if we have reached the end of the file
                break
            sequences.append(seq) # If not, appedning the data to the empty lists
            qualities.append(qual)
    return sequences, qualities


seqs , quals = readFastq("SRR835775_1.first1000.fastq")

# print(seqs[:5])
# print(quals[:5])

def QtoPhred33(Q):
    return chr(Q + 33) # Converts quality to phred integer

def Pred33toQ(Q):
    return ord(Q) - 33 # Converts phred to quality integer

print(Pred33toQ("?"))
print(Pred33toQ("J")) # High quality

# This functions returns all the differnet types of qualities that where found in the file
def createHist(qualities):
    hist = [0] * 50 # creating the histrogram itself
    for qual in qualities:
        for phred in qual:
            q = Pred33toQ(phred) # converting quality to a number 
            hist[q] += 1
    return hist

h = createHist(quals)
# print(h)        

'''
# Plotting the ranges of qualities that were retruned in the histrogram
import matplotlib.pyplot as plt # Need to install the right environment to actually see the graph
plt.bar(range(len(h)), h) # plotting a bar chart and setting x and y values
plt.show()
'''

# This function will analyze the GC content in the sequnces
def findGCByPos(reads):
    gc = [0] * 100 # all the reads are 100 in length
    totals = [0] * 100

    for read in reads:
        for i in range(len(read)):
            if read[i] == 'C' or read[i] == 'G':
                gc[i] += 1 # if the letter is a C or G, the GC array will increase by 1 
            totals[i] += 1

    for i in range(len(gc)):
        if totals[i] > 0: # to avoid dividing by 0
            gc[i] /= float(totals[i])

    return gc

gc = findGCByPos(seqs)
print(gc)

# Figuring out the distribution of neucleotides in the genome
import collections
count = collections.Counter()
for seq in seqs:
    count.update(seq)
print(count)