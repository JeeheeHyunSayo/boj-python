import sys
input = sys.stdin.readline

# 테스트 케이스의 수
t = int(input())

for _ in range(t):
    # 의상의 수
    n = int(input())

    # 의상의 종류, 수
    my_dict = {}
    for _ in range(n):
        c, v = input().split()
        if v in my_dict:
            my_dict[v] += 1
        else:
            my_dict[v] = 1

    result = 1
    for c in my_dict.values():
        result *= (c+1)

    print(result - 1)