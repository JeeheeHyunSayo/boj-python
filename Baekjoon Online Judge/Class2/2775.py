
n = int(input())
for _  in range(n):
    a = int(input())
    b = int(input())

    ####
    arr = [i for i in range(1, b+1)]
    # print(arr) [1,2,3] 0층 3호실

    for _ in range(a): # 층
        for i in range(1, b): # 호 3층 = 1층 + 2층, b층 = 1층 ... + + b-1층
            arr[i] += arr[i-1]
            # print(i, arr[i])

    print(arr[-1]) # 마지막 원소 