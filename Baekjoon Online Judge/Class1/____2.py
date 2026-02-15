num = int(input())
for n in range(1, num+1):
    star = '*' * n
    space = " " * (num - n) # 공백
    print(space + star)
