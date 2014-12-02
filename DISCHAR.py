__author__ = 'dell'

loop = int(raw_input())
while loop!=0:
    loop-=1
    dict = {}
    inp_str = raw_input()
    for i in range(len(inp_str)):
        if inp_str in dict.values():
            dict[inp_str[i]]+=1
        else:
            dict[inp_str[i]]=1
    print len(dict)


