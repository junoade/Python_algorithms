#################################################### 
#
#   TODO 한번 더 풀어 체화할 것 
# 
#   이코테 ch04 실전 - 왕실의 나이트
#   8x8 체스판에서 나이트가 움직일 수 있는 경우의 수 반환하기 
#   > 검색 : a1 과 같이 받았을 때 'a', 1 로 나누기 
#
#################################################### 

N = str(input())

def solution(n):
    size = 8
    cnt = 0 

    # 중심을 기준으로 나누기
    cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    col_idx = N[:len(N)//2]
    col = cols.index(col_idx) + 1
    row = int(N[len(N)//2:])

    # 나이트가 움직일 수 있는 상대 거리 나열 
    # row, col 순 
    # 수직 이동 후 위 아래 한칸 
    moves = [(-2, -1), (-2, 1), (2, -1), (2, 1)]
    # 수평 이동 후 위 아래 한칸
    moves += [(-1, -2), (1, -2), (-1, 2), (1, 2)]
    print(moves) 
    
    # 경우의 수에 대해 확인하기
    for move in moves:
        # 현재 위치 + 움직일 수 있는 거리 
        next_row = row + move[0]
        next_col = col + move[1]

        # 검증 후 cnt 증가 시키기 
        if(next_row >= 1 and next_row <= size and next_col >= 1 and next_col <= size):
            cnt += 1
        
    return cnt

def first_solution(n):

    size = 8
    cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    # 중심을 기준으로 나누기
    col = N[:len(N)//2]
    row = int(N[len(N)//2:])
    
    col_idx = cols.index(col) + 1
    cnt = 0

    '''
    > 너무 복잡함 
    '''
    # 나이트가 수평으로 2칸식 이동할 수 있을 때 
    # if col_idx >= 2 and col_idx <= 6:
    #     # 수평 이동 후 수직으로 한칸 이동 시 

    #     # 모두 가능
    #     if row >= 2 and row <= 7:
    #         cnt += 2
    #     # down 만 가능
    #     elif row == 1:
    #         cnt += 1
    #     # up 만 가능
    #     elif row == size:
    #         cnt += 1

    # 나이트가 수직으로 2칸식 이동할 수 있을 때 
    # if row >= 3 and row <= 6:
    #     # 수평 이동 한칸이 가능할 때

    #     # 모두 가능
    #     if col_idx >= 2 and col_idx <= 7:
    #         cnt += 2
    #     elif col_idx == 1:
    #         cnt += 1
    #     elif col_idx == size:
    #         cnt += 1

print(solution(N))