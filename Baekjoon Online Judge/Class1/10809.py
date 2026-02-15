
import sys


if __name__ == '__main__':
    input = sys.stdin.readline
    s = input().rstrip()
    # 97 (a) ~ 122 (z)
    alpha = [ chr(n) for n in range(97, 123)]
    for a in alpha:
        if a in s:
            print(f'{str(s.index(a))} ', end='')
        else:
            print('-1 ', end='')


