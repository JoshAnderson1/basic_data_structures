fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    #only interested in lines that have from as first word
    if not line.startswith("From "): continue
    #counter
    count = count + 1
    # splits each line that has from in it
    pieces = line.split()
    #this prints out the email address
    words = pieces[1]
    print(words)
print("There were", count, "lines in the file with From as the first word")
