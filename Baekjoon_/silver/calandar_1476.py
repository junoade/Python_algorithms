# bruteforce algorithm 전역탐색
# 1476

E, S, M = map(int, input().split())

year=0
e=0
s=0
m=0
while(True):
    if(e==16):
        e=1
    if(s==29):
        s=1
    if(m==20):
        m=1
    if(e==E and s==S and m==M):
        break
    year+=1
    e+=1
    s+=1
    m+=1

print(year)