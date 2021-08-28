
target = 20
fibseq=[0,1]
for x in range(target-2):
    fibseq.append(fibseq[-2]+fibseq[-1])
print("Sequence: {}".format(fibseq))
