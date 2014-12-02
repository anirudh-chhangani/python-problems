__author__ = 'anichhangani'
def func(H,U,D):
    res=H/U
    #print res
    if (H%U!=0 and H%D!=0) and (D%H!=0 and U%H!=0):
        return -1
    else:
        pos=H-H%U
        #print pos
        while pos!=H:
            if pos>H:
                pos-=D
                res+=1
            else:
                pos+=U
                res+=1

            #print pos
        return res

loop = int(raw_input())
while loop!=0:
    loop-=1
    arr = raw_input().split(" ")
    arr = map(int, arr)
    res = func(arr[0],arr[1],arr[2])
    print res
