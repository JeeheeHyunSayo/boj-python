n, m = map(int, input().split())

# 어떤 수의 약수는 해당 수의 제곱근 이하의 약수를 갖음(소수 힌트)
for i in range(n, m+1):
    if i < 2:
        continue
    flag = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i)
