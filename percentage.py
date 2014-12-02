__author__ = 'dell'
loop = int(raw_input())
dict = {}
arr = []
while loop!=0:
    loop-=1
    count=0
    arr = raw_input().split(" ")
    i=len(arr)-1
    while i!=0:
        count+=int(arr[i])
        #print count
        i-=1
        #print i
    dict[arr[0]]=int(count)
query = raw_input()
print "%.2f"%(dict[query]/3)


