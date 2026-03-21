import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    while True:
        s = input().rstrip()
        if s == '0': break
        if s == s[::-1] : print("yes")
        else: print("no")