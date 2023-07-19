def dynamic_programming(nums):
    n = len(nums)
    dp = [0] * n
     dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
     for i in range(2, n):
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])
     return dp[n-1]
 # 示例用法
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = dynamic_programming(numbers)
print("最大和为:", result)