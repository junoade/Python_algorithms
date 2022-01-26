################################################
#
# 1012 번 유기농 배추
# 유형 : 그래프 탐색, DFS
# 풀이 시간 : 27분 
# 비슷한 풀이 : DFS_Icecream 
# 결과 : Recursive Error 가장 많이 발생하는 이유는 Python이 정한 최대 재귀 깊이보다 재귀의 깊이가 더 깊어질 때입니다.
# 해결 : 재귀호출 스택 제한을 해제해줌 -> PASS 
# 
# 풀이
# 
#
################################################
import sys
sys.setrecursionlimit(10**6)

T = int(input())  # 테스트 케이스 개수

def dfs_main(graph, N, M):
    result = 0 
    for i in range(N):
        for j in range(M):
            if dfs(graph, i,j, N, M) == True:
                result += 1
    return result


def dfs(graph, x, y, N, M):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(graph, x-1, y, N, M)
        dfs(graph, x, y-1, N, M)
        dfs(graph, x+1, y, N, M)
        dfs(graph, x, y+1, N, M)
        return True
    return False


for _ in range(T):
    N, M, AMOUNT = map(int, input().split())  # 행, 렬, 배추 개수
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(AMOUNT):
        x, y = map(int, input().split())
        graph[x][y] = 1
    print(dfs_main(graph, N, M))
