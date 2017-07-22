fname = input("Enter file name: ")
fh = open(fname)
hour_count = dict()
for line in fh:
    #only want lines with From, skip other lines
    if not line.startswith("From "): continue
    #breaking down lines into times sent
    time = line.split()[5]
    #only want the hour from eaach time
    hours = time.split(':')[0]
    #made dict of hours
    if hours in hour_count:
        hour_count[hours] = hour_count[hours] + 1
    else:
        hour_count[hours] = 1
#printing out sorted dict by using tuples, lowest hour to highest hour
for key, val in sorted(hour_count.items()):
    print(key, val)
