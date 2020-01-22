# -- cornor case: existing 0 in nums  

# def numsayProdExpSelf(nums):
#     n = len(nums)
#     res = 1 
#     ans = nums 
#     for i in range(n):
#         res *= nums[i] 
#     for i in range(n):
#         ans[i] = res//nums[i] 
#     return ans 


def numsayProdExpSelf(nums):
    n = len(nums)
    L, R, ans = [1] * n, [1] * n, [1] * n 

    for i in range(n):
        for j in range(i):
            L[i] *= nums[j]
        for j in reversed(range(n-1-i)): 
            R[i] *= nums[n-1-j]
        ans[i] = L[i]*R[i]
    return ans  
    
        
example = [1, 2, 3, 4, 5] 
print(example)
print(numsayProdExpSelf(example)) 

example = [1, 2, 0, 4, 5] 
print(example)
print(numsayProdExpSelf(example)) 

