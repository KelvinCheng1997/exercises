import math
power = 3
digitlist=[]
result=0
for x in range(10**(power-1),10**power):
    xs = list(str(x))
#    result = int(xs[0])**5 + int(xs[1])**5 + int(xs[2])**5 + int(xs[3])**5 + int(xs[4])**5
    ''' I am her
        you are there
    '''
    for y in xs:
        result = result + int(y)**power
    if x==result:
        digitlist.append(x)
    result=0

print(digitlist)
print("The final sum: {}".format(sum(digitlist)))

