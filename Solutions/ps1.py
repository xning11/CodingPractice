def twoSum(mylist, k):
    res = {} 
    if len(mylist) == 0:
        return ValueError("The input is empty.")
    else: 
        for i in range(len(mylist)):
            res[mylist[i]] = k - mylist[i] 
            if (k-mylist[i]) in res: 
                return True  
        return False  
            

input = [10, 15, 3, 7] 
target = 17             
            
print(twoSum(input, target)) 
print(twoSum(input, 12)) 
print(twoSum([], target)) 

