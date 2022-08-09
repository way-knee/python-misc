def rd(nums):
    k = len(nums)        
    i = 0

    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            nums[i] = None
            k -= 1
        i += 1

    def isNone(nums):
        for x in range(k,len(nums)):
            if nums[x] is not None:
                return False
        return True

    while not isNone(nums):
        for n in range(len(nums)-1):
            if nums[n] is None and nums[n+1] is not None:
                nums[n] = nums[n+1]
                nums[n+1] = None
    return nums, k

l = [0,0,1,1,1,2,2,3,3,4]

