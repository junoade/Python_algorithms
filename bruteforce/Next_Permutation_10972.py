################################################
#
#   백준 10972 - 다음 순열 문제 - Bruteforce 유형
#   회독 : 1회차
#   풀이 시간 : over 
#   
#   핵심
#   1) 순방향으로 arr[i] < arr[i+1] 인 조합 중 가장 마지막 조합의 idx를 구한다. ( 놓치지 말자 )
#   2) 그 다음 arr의 끝에서 j 인덱스와 idx 의 값을 비교한다.
#   3) 만약 arr[j] > arr[idx] 라면
#      앞서 선행된 숫자들 보다 크며 아직 이동하지 않은 숫자라고 여길 수 있다.
#   4) swap 하고, 해당 idx 까지 리스트와 idx+1이후 부터 마지막까진 정렬하여 사전 순 조건을 만족시켜준다.
#
################################################

N = int(input())
arr = list(map(int, input().split()))


# 순방향으로 arr[i] < arr[i+1] 인 모든 값들 중 마지막 idx를 구한다
idx = -1 
for i in range(N-1):
    if arr[i] < arr[i+1]:
        idx = i

if idx == -1:
    print(-1)
else:
    # 끝 방향 인덱스 j의 값과 i의 값을 비교하고
    # arr[j] > arr[i] 라면 swap한 다음
    # i+1 부터 마지막 인덱스까지 정렬 한다.
    for j in range(N-1, 0, -1):
        if arr[j] > arr[idx]:
            arr[idx], arr[j] = arr[j], arr[idx]
            arr = arr[:idx+1] + sorted(arr[idx+1:])
            print(*arr)
            break



# def first_failed():
#     cnt = 0
#     i = -1
#     while cnt != N-2:
#       if arr[i-2] > arr[i-1] and arr[i-1] > arr[i]:
#           i -= 1
#           cnt += 1
#       else:
#           if arr[i-2] > arr[i-1] and arr[i-1] < arr[i]:
#               # swap 
#               arr[i-1], arr[i] = arr[i], arr[i-1]
#           elif arr[i-2] < arr[i-1] and arr[i-1] > arr[i]:
#               # swap
#               arr[i-2], arr[i] = arr[i], arr[i-2]
#           elif arr[i-2] < arr[i-1] and arr[i-1] < arr[i]:
#               arr[i-1], arr[i] = arr[i], arr[i-1]
#           break

# # 출력 
# if cnt == N-2:
#         print(-1)
# else:
#     for i in arr:
#         print(i, end=" ")

        

