fname = input("Enter file name: ")
fh = open(fname)
words = list()
for line in fh:
    #goes through each word
    for word in line.split():
        #checks if word is in list
        if not word in words:
            #if not in list appends to list
            words.append(word)
words.sort()
print(words)
