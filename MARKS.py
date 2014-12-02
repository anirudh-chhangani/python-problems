__author__ = 'dell'

loop  = int(raw_input())
subjects = [""]*5
ten_perc = loop/10
temps = []
while loop!=0:

    loop-=1
    inp = raw_input()
    temps = inp.split(" ")
 #   print temps
    if temps[0] == "A":
        subjects[0]+=temps[1]+" "
    elif temps[0] == "B":
        subjects[1]+=temps[1]+ " "
    elif temps[0] == "C":
        subjects[2]+=temps[1]+" "
    elif temps[0] == "D":
        subjects[3]+=temps[1]+" "
    elif temps[0] == "E":
        subjects[4]+=temps[1]+" "
#print subjects

for i in range(len(subjects)):
    temps2 = subjects[i].split(" ")
    if len(temps2)>ten_perc:
        temps2 = [str for str in temps2 if str]
        for i in range(len(temps2)):
            temps2[i]=int(temps2[i])
        if len(temps2)==0:
            print "Nothing Unusual"
        else:
            temps2 = list(set(temps2))
            for i in range(len(temps2)):
                if i == len(temps2)-1:
                    print(temps2[i])
                else:
                    print(temps2[i]),