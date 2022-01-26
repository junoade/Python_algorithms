####################################
#   이코테 - ch05 DFS/BFS - 음료수 얼려먹기
#   1. 재귀적 풀이
#   2. 모든 좌표에 대해 DFS 탐색
#
####################################

# 행 렬 입력받음
N, M = map(int, input().split())
graph = []

for i in range(N):
    graph.append(list(map(int, input())))

# 전역 변수 map을 이용
# 재귀적 풀이
def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M: # 좌표 검증
        return False
    
    # 현재 노드가 아직 방문하지 않은 노드라면
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상 하 좌 우 좌표에 대해서도 모두 재귀적으로 DFS 탐색해 줌
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True # 여기까지 도달하면 True
    
    return False # 이미 방문했거나 칸막이라면 False
        

# main 부
result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)
