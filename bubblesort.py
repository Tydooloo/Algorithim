

def bubble_sort_low_high(num):
    for i in range(len(num)):
        for j in range(len(num) - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num

def bubble_sort_high_low(num):
    for i in range(len(num)):
        for j in range(len(num) - 1):
            if num[j] < num[j + 1]:  
                num[j], num[j +1] = num[j + 1], num[j]
    return num





nums = [6,5,3,1,8,7,2,4,3,2,6,4,2,7,8,2]


def bubble_sort_low_highv2(num):
    for i in range(len(num), 0, -1):
        for j in range(i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num

def bubble_sort_high_lowv2(num):
    for i in range(len(num)):
        for j in range(len(num) - 1):
            if num[j] < num[j + 1]:  
                num[j], num[j +1] = num[j + 1], num[j]
    return num


for j in range(len(nums), 0, -1):
    pass


nums = [2,4,5,6,1,5,3,4,3,2,6,4,2,5,7,8]


for i in range(len(nums)-1):
    if nums[i] > nums[i+1]:
        temp = nums[i]
        nums[i] = nums[i+1]
        nums[i+1] = temp
print(nums)
        
