n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(input())

# n * m 보드에서 8 * 8 을 자르면
# 시작 좌표 (i, j) : i ~ n-8, j ~ m-8
# (i, j) 를 왼쪽 위 꼭짓점으로 하는 8 * 8 모두 탐색

# 1, n-8+1, (i, j) 는 시작점
result = 64 # 최대는 다 칠하는 거
for i in range(n-7):
    for j in range(m-7):
        # i,j 는 8 * 8 체스판 후보
        cnt_b = 0 # b로 시작하는 체스판의 틀린것의 개수를 세기
        cnt_w = 0
        for x in range(8):
            for y in range(8):
                # 홀수 위치, 짝수 위치로 구분
                if (x + y) % 2 == 0:
                    if arr[i+x][j+y] != 'B':
                        cnt_b += 1
                    if arr[i+x][j+y] != 'W':
                        cnt_w += 1

                else:
                    if arr[i+x][j+y] != 'W':
                        cnt_b += 1
                    if arr[i+x][j+y] != 'B':
                        cnt_w += 1
        # w, b 가정, 둘 중 가장 적게 칠한 최소의 수 ㄱㄱ
        result = min(cnt_b, cnt_w, result)
print(result)





