#################################################### 
#
#   TODO 한번 더 풀어 체화할 것
#   이코테 ch4 - 04 게임 개발
#   유형 : 시뮬레이션 
#   시간 : 1회차) 46/40
#
#   요약)
#   N*M 2차원 공간을 첫번째 입력, 2차원 좌표, 방향 을 두번째 입력,
#   좌표공간의 육지, 바다 공간에 대해 세번째부터 입력으로 받는다
#   
#   현재 위치에서 현재 방향을 기준으로 왼쪽(반시계 방향으로 90도)회전하고 난 후의
#   왼쪽칸이 visit하였는지, 바다인지 육지인지에 따라 주어진 규칙에 따라 진행
#
#################################################### 


N, M = map(int, input().split())
r0, c0, d0 = map(int, input().split())

map_info = []
for i in range(N):
    map_row = list(map(int, input().split()))
    if M != len(map_row) : 
        print("입력 오류")
        break
    else:
        map_info.append(map_row)

#init_size = (N, M)
#init_pos = (r0, c0, d0)
def solution(init_size,init_pos, m_info):
    
    # 방문한 위치를 저장하는 visit_map
    # N * M 사이즈
    visit = [[0] * init_size[1] for _ in range(init_size[0])]

    # 북동남서 좌표 이동를 위한 리스트
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # 북동남서 방향의 d값
    direction = init_pos[2]
    now_r = init_pos[0]
    now_c = init_pos[1]

    # 결과값 
    visit_cnt = 1 # 초기 위치도 방문이라고 치면
    turn_limit = 0
    
    while True:
        
        # 1) 왼쪽 방향으로 회전
        # 북 -> 서 -> 남 -> 동 
        if direction == 0: # 북쪽 에서 서쪽으로 
            direction = 3
        else:
            direction -= 1

        # 왼쪽 한칸의 좌표 갱신 
        temp_r = now_r + dr[direction]
        temp_c = now_c + dr[direction]

        # 2) 왼쪽 칸이 육지이거나 아직 visit 하지 않았으면
        # 그렇다면 회전(1) 이후 왼쪽으로 한칸 전진
        if m_info[temp_r][temp_c] == 0 and visit[temp_r][temp_c] == 0:
            # 방문 기록 갱신 
            visit[temp_r][temp_c] = 1
            visit_cnt += 1 
            turn_limit = 0

            now_r = temp_r
            now_c = temp_c
            continue
        # 왼쪽 칸이 바다이거나, 방문한 장소라면 turn_limit 증가
        # 결론적으로 회전을 반복하며 왼쪽칸을 점검하게 됨
        else: 
            turn_limit += 1
        
        # 3) 네방향 모두 가본 칸 또는 바다라면, 한칸 뒤로 가고 1단계로 간다.
        # 뒤칸이 바다라면 종료한다.
        if turn_limit == 4:
            temp_r = now_r - dr[direction] 
            temp_c = now_c - dr[direction]
            
            #뒤칸이 육지라면
            if m_info[temp_r][temp_c] == 0:

                # 뒤칸으로 가는 것 역시 visit_cnt의 증가로 봐야하지 않을까?
                # visit_cnt += 1

                now_r = temp_r
                now_c = temp_c 
            else:
                break
            turn_limit = 0   # 초기화

    return visit_cnt

# solution 호출
init_size = (N,M)
init_pos = (r0, c0, d0)
print(solution(init_size, init_pos, map_info))


     


            




    





