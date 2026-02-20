import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    s = input().rstrip()
    mod = 1234567891

    alpha = [chr(i) for i in range(97, 123)]
    num = [i for i in range(1, 27)]

    dict = {}
    for k, v in zip(alpha, num):
        dict[k] = v

    answer = 0
    for i in range(len(s)):
        answer += (dict[s[i]] * pow(31, i, mod)) % mod
    print(answer % mod)
