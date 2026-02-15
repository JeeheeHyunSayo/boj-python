import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    while True:
        a, b, c = map(int, input().split())
        if a==0 and b == 0 and c == 0 : break
        max_val = a
        if max_val > b and max_val > c:
            max_val = a
            if max_val ** 2 == (c**2) + (b**2):
                print("right")
            else:
                print("wrong")
        elif max_val < b and c < b:
            max_val = b
            if max_val ** 2 == (a**2) + (c**2):
                print("right")
            else:
                print("wrong")
        else:
            max_val = c
            if max_val ** 2 == (a**2) + (b**2):
                print("right")
            else:
                print("wrong")


