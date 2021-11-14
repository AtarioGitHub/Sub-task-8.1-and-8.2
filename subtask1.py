import math

n = input('Enter your number which we will call n = ') 
print('n = ',n)

DecimalNumberofN = float(n) # We use float so that we can also use a decimal value

TheSquareRootofThatNumber = math.sqrt(DecimalNumberofN)
xyz = int(TheSquareRootofThatNumber) # Let xyz be an integer value  

q=pow(xyz,2)

print('q = ', q) 