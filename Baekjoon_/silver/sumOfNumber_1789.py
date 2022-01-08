S = int(input())

k=1
sum=0
while(True):
    sum += k
    if( sum > S):
        k -=1
        break
    else:
        k+=1

print(k)