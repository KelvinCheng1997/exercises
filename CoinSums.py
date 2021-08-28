target=80
coinlist=[1,2,5,10,20,50,100,200]
resultlist=[]
way=0
for a in range(target+1):
    for b in range(target//2 + 1):
        for c in range(target//5 + 1):
            for d in range(target//10 + 1):
                for e in range(target//20 + 1):
                    for f in range(target//50 + 1):
                        for g in range(target//100 + 1):
                            for h in range(target//200 + 1):
                                result =  a + b*2 + c*5 + d*10 + e*20 +f*50 + g*100 + h*200
                                if result == target:
                                    #resultlist.append((a,b,c,d,e,f,g,h))
                                    way+=1
                                    #print((a,b,c,d,e,f,g,h))

                                result = 0

#print("The combination: {}".format(len(resultlist)))
print("The combination: {}".format(way))
print(resultlist)