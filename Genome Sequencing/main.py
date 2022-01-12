'''
String S --> a finite sequence of characters, Z = {A, C, G, T}
|S| --> number of characters in S, len(s)
e --> empty string |e| = 0, len(" ")
Character Offset --> getting index of an element in a list, a_list[0]
Substring --> a smaller string inside a bigger string, s[2:6] inside s = 'AACCGGTTA'
Prefix of S --> a substring starting at the beginning of S, s[0:6] or s[:6]
Suffix --> a substring ending at end of S, s[-4] or s[len(s)-4]
'''

#Ex 1
seqx = "ACGT"
seqx[1] #C
len(seqx) #4
e = " "
len(e) #0

seq1 = "CCAA"
seq2 = "GGTT"
seq3 = seq1 + seq2 #concatination

seqs = ['A', 'C', 'C', 'G']
a_seq = ''.join(seqs) #concatination with no commas, ACCG

import random
# random.seed(7) #this will give a certain letter every time
# random.choice('ACGT') #randomly chooses a letter out of ACGT

# Way 1
seq = ''
for _ in range(10): # We use an underscore whewn we don't care about the indexation
    seq += random.choice('ACGT')
# print(seq)

# Way 2
seq4 = " ".join([random.choice('ACGT') for _ in range(10)])
# print(seq4)

seq4[1:5] #subscript
seq4[:5]  #prefix
seq4[7:]  #suffix
seq4[-3:] #suffix

def longestCommonPrefix(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2:
        i += 1
    return s1[:i]

a = longestCommonPrefix('ACCATGT', 'ACCAGAC')
print(a)

# Way 1
def match(s1, s2):
    if not len(s1) == len(s2):
        return False
    
    for i in range(len(s1)):
        if not s1[i] == s2[i]:
            return False

    return True

z = match('ATTCC', 'ATTCCGGT')
print(z)

# Way 2
'ACCTG' == 'AYTTF'

# Example 2
complement = {
    'A' : 'T',
    'T' : 'A',
    'C' : 'G',
    'G' : 'C'
}

def reverse(s):
    t = ''
    for base in s:
        t = complement[base] + t #we're accessing the values in the dictionary
    return t

y = reverse('ACCTGGCCTAA')
print(y)

# Working with a real genome
def readGenome(filename):
    genome = " " #defining and empty string
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>': #making sure that the program starts reading the dile from the bases "Ex: ACTG"
                genome += line.rstrip() #rstrip removes any unwanted whitespace

    return genome

genome = readGenome('lambda_virus.fa') #passing the file to the function


# Counting the number of times each base occurs in the genome

# Defininf a dictionary and setting the initial frequency count to 0

# Way 1
countss = {
    'A' : 0,
    'C' : 0,
    'G' : 0,
    'T' : 0, 
    ' ' : 0
}
for base in genome:
    countss[base] += 1 #incrementing the frequency count 
print(countss)

# Way 2
import collections
print(collections.Counter(genome))