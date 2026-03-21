import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    s = input().rstrip()
    mod = 1234567891
    r = 31

    answer = 0
    power = 1

    for ch in s:
        value = ord(ch) - 96 # 1~ 26
        answer = (answer + value  * power)  % mod
        power = (power * r) % mod # power = 31 ** i 의 역할. .

    print(answer)
