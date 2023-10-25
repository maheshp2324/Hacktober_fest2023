# Kadane's Algorithm - gfg problem solution


class Solution:
   
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        if not arr:
            return 0
        max_sum = arr[0]
        current_sum = arr[0]
        
        for num in arr[1:]:
            current_sum = max(num , current_sum + num)
            max_sum  = max(max_sum , current_sum)
            
        return max_sum
