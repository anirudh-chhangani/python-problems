__author__ = 'dell'

input=  raw_input().split(" ")
input = map(int, input)
width = []
index = []

width = map(int, raw_input().split(" "))
while input[1]!=0:
    input[1]-=1
    index = map(int, raw_input().split(" "))
    #i+=1
    temps = width[index[0]:index[1]+1]
    wide = min(temps)
    if wide==1:
        print("1")
    if wide==2:
        print("2")
    if wide==3:
        print("3")