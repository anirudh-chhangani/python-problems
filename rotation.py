string = raw_input()
#print len(string)
pattern = raw_input()
for i in range(len(string)-1):
    string = string[len(string)-1]+string[0:len(string)-1]
    #print string
    if pattern == string:
        print "YES"