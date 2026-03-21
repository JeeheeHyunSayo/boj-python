import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    while True:
        a, b, c = map(int, input().split())
        if a == b == c == 0 : break

        sides = sorted([a,b,c]) # 배열 바로 대괄호 때려 버려
        if sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2 : print("right")
        else: print("wrong")