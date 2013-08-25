import heapq

fileHandle = open ('lorem.txt')
text = fileHandle.read()
fileHandle.close()


#Tree constructor
def createTree(symbol):
    trees = list(symbol)
    heapq.heapify(trees)        #transform the list into the "heap"
    while len(trees) > 1:
        #remove smallest item from "heap" and return, assign to left or right node
        left, right = heapq.heappop(trees), heapq.heappop(trees)    
        #parent node is combned frequencies of popped nodes and retains child nodes [newFreq,child1,child2]
        parent = [left[0] + right[0], left, right]
        #push the parent node back into the heap
        heapq.heappush(trees, parent)
    return trees[0]


symbolNew = []
def printTree(tree, prefix = ''):
    if len(tree) == 2:
        print tree[1], prefix
        #create dictionary for key to write into file
        insertion = (tree[1], prefix)
        symbolNew.append(insertion)
    else:
        #throw in left children and add 0 to prefix as we are traveling left
        printTree(tree[1], prefix + '0')
        #throw in right children and add 1 to prefix as we are traveling right
        printTree(tree[2], prefix + '1')
   
#===============================================================================
# First we need to construct a list of [frequency, symbol/character]
#===============================================================================

symbol = []
insertion = [0, 0]  #will be of the form (freq, symbol)
c = 0
for i in text:       #generate a list of all possible symbols
    for x in range(0, len(symbol)):
            if symbol[x][1] == i:
                c = 1
    if c == 0:
        insertion = [0.000, i]
        symbol.append(insertion)
    insertion = [0,0]
    c = 0
key = 'abcdefghijklmnopqrstuvwxyz'
key2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
given = [0.0817,0.0145,0.0248,0.0431,0.1232,0.0209,0.0182,0.0668,0.0689,0.0010,0.0080,0.0397,0.0277,0.0662,0.0781,0.0156,0.0009,0.0572,0.0628,0.0905,0.0304,0.0102,0.0264,0.0015,0.0211,0.0005]
#iterate through to replace lowercase with upper case
for i in text:
    for x in range(0, len(key)):
        if i == key[x]:
            i = key2[x]

for i in text:          #iterate through to get a count of all symbols
    for x in range(0, len(symbol)):
        if symbol[x][1] == i:
            symbol[x][0] += 1
            
for x in range(0, len(symbol)):     #go back through and calculate the percentage/frequency
    symbol[x][0] = symbol[x][0]/4007.00
#go back through to enter given frequencies..
for x in range(0, len(symbol)):
    for i in range(0, len(key2)):
        if x == key2[i]:
            x = given[i]

t = createTree(symbol)        #construct huffman tree
printTree(t)
print symbolNew

#===============================================================================
# Create binary 'compressed' file
#===============================================================================
#new string that will be written to new file
text2 = ''
#iterate through to create new string given huffman code values
for i in text:
    for x in range(0, len(symbolNew)):
        if i == symbolNew[x][0]:
            text2 += symbolNew[x][1]
print text2
#create new file and write text2 to it
fileHandle = open ('givenFrequencies.txt', 'w')
text = fileHandle.write(text2)
fileHandle.close()

    
