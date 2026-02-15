import sys

def solution(n):
    if 90 <= n <= 100:
        return 'A'
    elif 80 <= n <= 89:
        return 'B'
    elif 70 <= n <= 79:
        return 'C'
    elif 60 <= n <= 69:
        return 'D'
    else:
        return 'F'

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    print(solution(n))