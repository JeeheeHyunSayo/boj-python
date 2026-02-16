import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    strn = str(n)
    length = len(strn)

    # 생성자가 없는 경우 산정을 안함
    for num in range(max(1, n - length*9), n):
        strnum = str(num)
        arr = [ int(s) for s in strnum]
        total = sum(arr)
        if n == (num + total):
            print(num)
            break
    else:
        print(0)