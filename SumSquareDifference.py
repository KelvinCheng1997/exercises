NaturalNum = 100
SumofSquares = 0
SquareofSum = 0
for x in range(1,NaturalNum+1):
    SumofSquares = SumofSquares + x**2
    SquareofSum = SquareofSum + x

print ("Different: {}".format(SquareofSum**2-SumofSquares))
