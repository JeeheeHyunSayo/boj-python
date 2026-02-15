import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        s = input().rstrip()
        score = 0
        count = 0
        for i in range(len(s)):
            if s[i] == 'X':
                count = 0
            if s[i] == 'O':
                count += 1
            score += count
        print(score)