# B = A * 1.1
# A % 100 = 0

# 1100 = 1000 * 1.1
# 1000 = 1100 *
def solution(n):
    price = int(n / 11 * 10)
    return price
num = int(input())
print(solution(num))