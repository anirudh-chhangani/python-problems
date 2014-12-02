__author__ = 'anichhangani'
#binary search tree
class node:
    def __init__(self, val = None, left=None, right=None ):
        self.val=val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)
head = node()

loop = int(raw_input())
num = map(int,raw_input().split(" "))
print num

def add2tree(num,curr):
    if curr.val >num:
        if curr.left==None:
            curr.left = node(num)
            print num
        else:
            add2tree(num,curr.left)
    else:
        if curr.val==num:
            return
        if curr.right==None:
            curr.right=node(num)
            print num
        else:
            add2tree(num,curr.right)


def build_tree(num):
    print(num)
    count = 0
    while count!=len(num):
        curr=head
        if head.val==None:
            head.val = num[count]
        else:
            add2tree(num[count],curr)
        count+=1

build_tree(num)
print
print "Now the tree would be as follows"
print
print "Root : "+str(head.val)
print "left : "+str(head.left.val)
print "right : "+str(head.right.val)
print "test : "+str(head.left.left.right)

