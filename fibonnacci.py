__author__ = 'dell'
iter = int(raw_input())

#recurrence...lookup table
lookup=[-1]*(iter+1)
#print (lookup)
lookup[0]=0
lookup[1]=1
def fibo(num):
    if lookup[num]>-1:
        return int(lookup[num])
    else:
        #print(num)
        lookup[num] = int(fibo(num-1))+int(fibo(num-2))
        return lookup[num]
        #print(lookup)

fibo(iter)

print(lookup)
print(lookup[iter])






