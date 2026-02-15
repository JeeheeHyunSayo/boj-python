import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, s = input().rstrip().split()
        n = int(n)
        for string in s:
            print(string * n, end='')
        print()
