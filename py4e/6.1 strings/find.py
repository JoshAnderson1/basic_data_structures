text = "X-DSPAM-Confidence:    0.8475"
#finds the colon
pos = text.find(':')
#only want the number so move one over from colon
piece = text[pos+1:]
#convert from string to float
value = float(piece)
print(value)
