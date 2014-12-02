__author__ = 'dell'

f = open('filename2')
tc = int(f.readline())
tci=1
while tc!=0:
    #print tc
    tc-=1

    arr=[]
    numbus = f.readline()
    #print numbus
    busrange = f.readline().split(" ")
    busrange = map(int, busrange)
    numcity = int(f.readline())
    while numcity!=0:
        numcity-=1
        count =0
        city = int(f.readline())
        i=len(busrange)-1
        while i>=0:
            low = busrange[len(busrange)-i-1]
            high = busrange[len(busrange)-i]
            #print low, high
            if city>=low and city<=high:
                count+=1
            i-=2
        arr.append(count)
    print "Case #"+str(tci)+":",
    #print len(arr),
    for i in range(len(arr)):
        print arr[i],
    print("")
    tci+=1
    space = f.readline()
f.close()