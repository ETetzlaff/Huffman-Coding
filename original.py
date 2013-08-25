#===============================================================================
# Create a binary file from original to compare
#===============================================================================
fileHandle = open ('lorem.txt')
original = fileHandle.read()
fileHandle.close()

ordConv = [] #list containing int values of each character
for i in original:
    ordConv.append(ord(i))
    
binConv = [] #list containing binary values of each character
for i in ordConv:
    binConv.append(bin(i))
newString = []
for i in binConv:
    newString.append(str(i))

#create text3 which will be binary values of original
text3 = ''
for i in newString:
    text3 += i
print text3
#create new file and write text3 to it
fileHandle = open ('lorum2.txt', 'w')
text = fileHandle.write(text3)
fileHandle.close()     
