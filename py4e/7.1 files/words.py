#find and prints words.txt in upper case
fname = input("Enter file name: ")
fh = open(fname)
#reads text
text = fh.read()
#strips away whitespace
text.rstrip()
#all text is in uppercase now
print(text.upper())
