import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())  # 층수, 각 층의 방수, 몇 번쨰 손님
    '''
    if n%h == 0:
        floor = h
        num = n // h
    else:
        floor = n % h
        num = n // h + 1
    '''

    # 숏코딩
    floor = (n - 1) % h + 1
    num = (n - 1) // h + 1


    # print(str(floor)+str(num).rjust(2, '0'))
    print(f"{floor}{num:02d}")

