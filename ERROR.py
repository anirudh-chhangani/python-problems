import sys

__author__ = 'dell'

loop = int(sys.stdin.readline().rstrip());
num =0 ;
while (loop != 0):
    loop = loop - 1
    string = sys.stdin.readline().rstrip()
    sub = "101"
    sub1 = "010"
    if sub in string:
        num = num+1
    elif sub1 in string:
        num = num+1
    if num>0:
        print "Good"
    else:
        print "Bad"
    num = 0