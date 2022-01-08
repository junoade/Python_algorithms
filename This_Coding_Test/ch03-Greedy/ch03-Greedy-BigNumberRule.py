# L,M,K = input().split(" ")
# L,M,K = int(L), int(M), int(K)
L,M,K = map(int, input().split(" "))
# inputs = int(input().split(" "))
values = list(map(int, input().split()))
# print(values)
answers = []

firstMax = max(values)
values.remove(firstMax)
secondMax = max(values)

cnt = 0
for val in range(M):
    if(cnt <= K-1):
        answers.append(firstMax)
        cnt +=1
    else:
        answers.append(secondMax)
        cnt = 0
    
# print(answers)
print(sum(answers))




# 1트
# max = max(values) # max 값을 가져옴
# max_idx = [i for i,v in enumerate(values) if v==max]
# answers = []
# cnt = 0
# for idx in range(M):
#     for val in max_idx:
#         if(cnt != K):
#             answers.append(values[val])
#             cnt += 1
#         else:
#             cnt = 0
#             break    
# print(answers)
