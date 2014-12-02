__author__ = 'dell'

inp_str = str(raw_input())
#print(inp_str[0])
count = 1
i=1
fres = 0
while i < len(inp_str):
    j=i
    while j < len(inp_str) and inp_str[j]=='a':
        if inp_str[j-1]=='a':
            count+=1
        j+=1
    i+=j;
    if fres<count:
        fres=count
        count=1
print fres
fstring=""
if fres==1:
    print('aa')
else:
    if fres>=len(inp_str):
        print ""
    else:
        for i in range(fres+1):
            #print i
            fstring+='a'


print fstring