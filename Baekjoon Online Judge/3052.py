import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    rest = set()
    for _ in range(10):
        n = int(input())
        rest.add(n % 42)
    print(len(rest))