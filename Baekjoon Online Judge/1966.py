from collections import deque
k = int(input())

for i in range(k):
    # 문서의 개수, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 queue에서 몇 번째에 놓여 져 있는지
    n, m = map(int, input().split())

    # 몇 번째 놓여져 있는지 궁금한 문서 : m 번째 문서가 언제 출력됬는지
    arr = list(map(int, input().split()))
    q = deque((v, i) for i, v in enumerate(arr))

    # 큐의 맨 앞 값을 갖고 오는 방법
    cnt = 0 # 출력 횟수, 한 테스트 케이스 마다
    while q:
        value, index = q.popleft()
        if any(value < v for v, _ in q):
            q.append((value, index))
        else:
            cnt += 1
            if index == m:
                print(cnt)
                break