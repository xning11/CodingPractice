def twoSum(mylist, k):
    res = {}
    for i,v in emunerate(mylist):
        if res[v] is None: 
            res[v] = k - mylist[i] 
        else:
            res[v] 
            
