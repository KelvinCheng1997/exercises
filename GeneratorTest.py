numofprime = 10001
startint = 3
primelist=[2]
isprime = True
while True:
    if len(primelist) == numofprime:
        print(primelist[numofprime-1])
        break

    for y in primelist:
        if startint % y == 0:
            isprime = False
            break

    if isprime == True:
        primelist.append(startint)

    isprime = True
    startint += 2



