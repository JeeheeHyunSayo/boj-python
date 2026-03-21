import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    num = 1
    for i in range(1, n+1):
        num *= i

    cnt = 0
    strNum = str(num)
    for j in strNum[::-1]:
        if j == '0':
            cnt += 1
        else:
            break

    print(cnt)
