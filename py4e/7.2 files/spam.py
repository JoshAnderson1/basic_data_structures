# Use the file name mbox-short.txt as the file name
#Asked us not use sum or sum() while calculating the average
fname = input("Enter file name: ")
fh = open(fname)
count = 0
x = 0
for line in fh:
    #only interested in lines that have "spam" in them
    if not line.startswith("X-DSPAM-Confidence:") : continue
    # keeping track of spam confidence
    x = float(line[20:].rstrip()) + x
    count = count + 1
avg = x/count
print("Average spam confindence: ", avg)
