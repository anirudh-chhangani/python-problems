loop = int(raw_input())
numer=0
while loop!=0:
	loop-=1
	string_inp = raw_input().split(".")
	teststr = string_inp[1]
	for i in range(len(teststr)):
		if teststr[i]=="a" or teststr[i]!='i' or teststr[i]!='o' or teststr[i]!='u' or teststr[i]!='e':
			numer+=1
	print numer+"/"+len(teststr)