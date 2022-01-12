'''
Exact matching --> at what offset does pattern P occur within text T?
'''
text = "there would have been a time for such a word"
print(len(text))
a = text.find("word")
print(a)

# Naive algorithm 
def naive (p, t):
    occurences =[]
    for i in range(len(t) - len(p) + 1): # This loop itereates over alignment from left to right
        match = True
        for j in range(len(p)): # This loop iterated over character comparisons from left to right
            if t[i+j] != p[j]:
                match = False
                break
        if match:
            occurences.append(i)
    return occurences

def possibleAlignments(x, y):
    x_len = len(x)
    y_len = len(y)
    while True:
        if y_len >= 0:
            return x_len/y_len

print(possibleAlignments("qwertyuiopas", "qwe"))