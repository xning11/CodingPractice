def twoSum(nums, k):
    res = {} 
    if not nums:
        return ValueError("The input is empty.")
    else: 
        for i in range(len(nums)):
            res[nums[i]] = k - nums[i] 
            if (k-nums[i]) in res: 
                return True  
        return False  
            

example = [10, 15, 3, 7] 
target = 17             
            
print(twoSum(example, target)) 
print(twoSum(example, 12)) 
print(twoSum([], target)) 

