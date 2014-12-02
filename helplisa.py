import sys

__author__ = 'dell'

loop = int(sys.stdin.readline().rstrip())

def calc(ax, ay, bx, by, cx, cy):
    res = (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)) / 2
    return res

arr2 = []
while loop != 0:
    arr = []
    tstr = ""
    num = str(sys.stdin.readline().rstrip())
    #print(num[:1])
    i = 0
    #print(num.__len__())
    for i in range(num.__len__()-1):
        if (num[i] != " "):
            if(num[i+1]!=" "):
                tstr += num[i]
            else:
                tstr += num[i]
                arr.append(tstr)
                tstr = ""

    tstr += num[num.__len__()-1]
    arr.append(tstr)
    #print(arr)
    res = calc(int(arr[0]), int(arr[1]), int(arr[2]), int(arr[3]), int(arr[4]), int(arr[5]))
    if(res>=0):
        arr2.append(res)
    else:
        arr2.append(res*-1)
    #arr2.sort()
    loop -= 1
arr3 = []

arr3 = list(arr2)
arr3.sort()
small = arr3[0]
large = arr3[arr3.__len__()-1]
#print(arr3)
for i in range(arr2.__len__()):
    if(arr2[i]==small):
        sindex = i
    if arr2[i]==large:
        lindex = i

print sindex+1, lindex+1

sys.exit()