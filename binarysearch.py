__author__ = 'dell'
from bisect import bisect_right


def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if a[i-1]==x:
        return a[i-1]
    if i != len(a):
        return a[i]
    #raise ValueError

box_numbers = int(raw_input())

pos = raw_input().split(" ")
print pos
pos1 = map(int, pos)

pro_size =int(raw_input())
res = find_gt(pos1, pro_size)
print res





