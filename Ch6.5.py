
str = " X-DSPAM-Confidenece: 0.8475 "

ipos = str.find(":")
piece = str [ipos + 2 : ]
#print(piece+42.0) # will fail
value = float(piece)
print(value)
print (value+42)