#from numpy.distutils.fcompiler import none
import sys

__author__ = 'dell'
loop = int(sys.stdin.readline().rstrip());

exp = 1;
res = 0;
n = 0;
while loop != 0:
    num = int(sys.stdin.readline().rstrip());
    loop = loop - 1
    for exp in range(1, 100):
    #print(exp)
        n = num / 5 ** exp;
        #print(num)
        if n == 0:
            break;
        else:
            res = res + n;
    print(res);
    res =0
print("hi")


