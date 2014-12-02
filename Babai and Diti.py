__author__ = 'dell'

loop = int(raw_input())
while loop!=0:
    arr = [-1]*10
    size = int(raw_input())
    arrlen = [0]*10
    loop=loop-1
    input_string = str(raw_input())
    array = input_string.split(" ")
    for i in range(len(array)):
        print i
        if arr[int(array[i])]==-1:
            arr[int(array[i])]= i
        else:
            arrlen[int(array[i])] = i - arr[int(array[i])]
    arrlen.sort()
    print arrlen[9]+1

