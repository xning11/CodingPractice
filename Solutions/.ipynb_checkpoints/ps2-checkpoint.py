# -- cornor case: existing 0 in array 

# def arrayProdExpSelf(arr):
#     lens = len(arr)
#     res = 1 
#     ans = arr 
#     for i in range(lens):
#         res *= arr[i] 
#     for i in range(lens):
#         ans[i] = res//arr[i] 
#     return ans 


def arrayProdExpSelf(arr):
    lens = len(arr)
    L, R, ans = [1] * lens, [1] * lens, [1] * lens 

    for i in range(lens):
        for j in range(i):
            L[i] *= arr[j]
        for j in reversed(range(lens-1-i)): 
            R[i] *= arr[lens-1-j]
        ans[i] = L[i]*R[i]
    return ans  
    
        
example = [1, 2, 3, 4, 5] 
print(example)
print(arrayProdExpSelf(example)) 

example = [1, 2, 0, 4, 5] 
print(example)
print(arrayProdExpSelf(example)) 

