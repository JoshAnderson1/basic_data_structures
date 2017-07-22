name = input("Enter a file name: ")
fh = open(name)
sender_count = dict()
for line in fh:
    #only want lines with "From " skip other lines
    if not line.startswith("From "): continue
    #puts the senders in dict
    sender = line.split()[1]
    if sender in sender_count:
        sender_count[sender] = sender_count[sender] + 1
    else:
        sender_count[sender] = 1
#finds the biggest sender
largest = -1
bestsender = None
for k,v in sender_count.items():
    if v > largest:
        largest = v
        bestsender = k
print(bestsender,largest)
