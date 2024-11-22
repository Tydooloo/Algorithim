nums = [2,1,4,3,5]

for i in range(len(nums) -1):
    print(nums[i])
    for j in range(1, len(nums)):
        #check all other elements
        increase = 0
        if nums[i] > nums[j]:
            increase += 1
    temp = nums[i]
    nums[i] = nums[i+increase]
    nums[i+increase] = temp 



        
print(nums)
