tc = int(raw_input())
arr = []
set = []
while tc!=0:
    tc=tc-1
    arr.append(int(raw_input()))
arr.sort()
arr.reverse()
iter = 3
for i in range(len(arr)):
    if i==3:
        break
    set.append(arr[i])
while iter<len(arr):
    set[2]+=arr[iter]
    set.sort()
    set.reverse()
    iter+=1
print set[0]
