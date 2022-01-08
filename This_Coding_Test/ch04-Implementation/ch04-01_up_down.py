####################################
#   이코테 - ch04 구현 1 - 상하좌우 문제
#   map -> list 검색함
#   11:28 분 소요 
#
####################################


N = int(input())
P = list(map(str, input().split()))

# map object is not subscriptable
# list등으로 캐스팅 할 필요가 있음
# print(P[0])

def solution(n, p):
    row = 1
    col = 1
    for i in range(len(p)):
        if p[i] == 'L' and col != 1:
            col -= 1
        elif p[i] == 'R' and col != n:
            col += 1
        elif p[i] == 'U' and row != 1:
            row -= 1
        elif p[i] == 'D' and row != n:
            row += 1

    print(f"{row} {col}")


solution(N, P)







