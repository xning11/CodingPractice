def numDecodings(s):
    if not s or s[0] == '0':
        return 0
    
    n = len(s)
    dp = [0 for x in range(n+1)]
    dp[0] = 1 
    
    for i in range(1, n+1):
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        if i != 1 and s[i-2:i] <= '26' and s[i-2:i] >= '10':
            dp[i] += dp[i-2]
    return dp[n]


if __name__ == "__main__":
    
    example = '226' 
    print(numDecodings(example)) 

    example = '102213' 
    print(numDecodings(example)) 
