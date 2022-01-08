# bruteforce algorithm 전역탐색
# 1476
# Test case

import time

def test(E, S, M):
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
    return year

for i in range(1,16):
    for j in range(1,29):
        for h in range(1,20):
            start = time.time()
            test(i,j,h)
            end = time.time()
            result=end-start
            if(result > 2.0):
                print("No Go - Time limitation Failed")
                break
            
print("test success")
