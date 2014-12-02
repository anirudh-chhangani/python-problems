'''
# Read input from stdin and provide input before running code

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
#print 'Hello World!'
jumps=0
loop = int(raw_input())
while loop!=0:
	loop-=1
	case = raw_input().split(" ")
	case = map(int, case)
	if case[0]>case[1]:
		temp = case[0]
		case[0] = case[1]
		case[1]=temp
	print case[1]/case[2]-(case[0]-1)/case[2]
print case
