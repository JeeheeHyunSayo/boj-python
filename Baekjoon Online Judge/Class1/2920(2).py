# 같은 값에 대한 모순 조건 검사로 인해서 아래의 flag 처리가 안된 것 .
# nums[i], nums[i-1] 의 검사가 필요 한 것

if __name__ == '__main__':
    arr = list(map(int, input().split()))

    # ascending, descending 따로 추적, True -> False 가 정석
    asc = True
    des = True

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            asc = False
        elif arr[i] > arr[i-1]:
            des = False

    if asc:
        print("ascending")
    elif des:
        print("descending")
    else:
        print("mixed")