def twoSum(arr, k):
    res = {} 
    if not arr:
        return ValueError("The input is empty.")
    else: 
        for i in range(len(arr)):
            res[arr[i]] = k - arr[i] 
            if (k-arr[i]) in res: 
                return True  
        return False  
            

example = [10, 15, 3, 7] 
target = 17             
            
print(twoSum(example, target)) 
print(twoSum(example, 12)) 
print(twoSum([], target)) 

