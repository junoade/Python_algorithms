# CH03 그리디 숫자 카드 게임
N,M = map(int, input().split())
array = [[0 for col in range(M)] for row in range(N)]
# array =[]
for i in range(N):
    array[i] = list(map(int, input().split()))
#    array.append(list(map(int, input().split())))
    
print(array)