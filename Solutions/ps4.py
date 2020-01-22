def firstMisPos(nums):
    # nums = [] or nums does not contain 1
    if 1 not in nums:
        return 1  
    
    n = len(nums) 
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n+1 
        
    for i in range(n): 
        idx = abs(nums[i]) - 1
        if idx < n:
            nums[idx] = - abs(nums[idx]) 
        
    for i in range(n):
        if nums[i] > 0:
            return i+1     
        
    return n+1 


if __name__ == '__main__':

    example = [3, 4, -1, 1]
    print(example)
    print(firstMisPos(example))

    example = [15,14,13,5,2,1] 
    print(example)
    print(firstMisPos(example))

    example = [] 
    print(example)
    print(firstMisPos(example))


# see --> https://leetcode.com/problems/first-missing-positive/discuss/17256/Short-python-solution-using-abs()/362986