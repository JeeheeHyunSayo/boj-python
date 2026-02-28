import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    a, b = tuple(map(int, input().split()))
    num = min(a,b)
    gcd = 0
    for i in range(1, num+1):
       if a % i == 0 and b % i == 0:
           gcd = i
    print(gcd)

    lcm = a * b // gcd
    print(lcm)