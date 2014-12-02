__author__ = 'dell'

def bitwise_xor(numa, numb):
    bres=""
    i=0
    j=0
    res = 0
    while numa!=0 or numb!=0:
        bna = numa%2
        bnb = numb%2
        bres += str(bna^bnb)
        i+=1
        #print i
        numa = int(numa/2)
        numb = int(numb/2)
    #print bres[::-1]
    #print bres
    for j in range(len(bres)):
        if bres[j]=='1':
            res+=pow(2,j)
        #print res
    return res



numa = int(raw_input())
numb = int(raw_input())
rnge = numb-numa
rnge+=1
rnge = rnge*rnge
a= numa
count=0
b=numa
resarr = [0]*rnge
k = 0
while a!=numb+1:
    while b!=numb+1:
        resarr[k] = bitwise_xor(a,b)
        count+=1
        k+=1
        #print(count)
        b+=1
    b=a
    a+=1
#print resarr
print max(resarr)