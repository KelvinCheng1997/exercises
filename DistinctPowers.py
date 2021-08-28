distinctset=set()
repeatorder=100
for a in range(2,repeatorder + 1):
    for b in range(2, repeatorder + 1):
        x = a**b
        distinctset.add(x)

#finalset=set(distinctlist)
print("Distince value: {}".format(len(distinctset)))
