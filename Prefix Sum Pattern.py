

# def sum_array(i, j):
#     array = [3,2,5,8,9,7,3]

#     b = sum(array[i:j +1])
#     return b

# print(sum_array(1,3))







# def create_prefix(arr):
#     for i in range(1, len(arr)):
#         arr[i] += arr[i-1]
#     return arr

# print(create_prefix([1,2,3,4,5,6,7,8]))


# Leetcode 303 dont understand solution at all
# class NumArray:

#     def __init__(self, nums):

#         self.prefix_sum = [0] * (len(nums) + 1)
#         print(self.prefix_sum)

#         for i in range(len(nums)):
#             # range(0,6)
#             self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]



#     def sumRange(self, left: int, right: int) -> int:
#         return self.prefix_sum[right + 1] - self.prefix_sum[left]




# nums = [-2, 0, 3, -5, 2, -1]
# numArray = NumArray(nums)

# # Perform the sumRange queries
# print(numArray.sumRange(0, 2))  # Sum of elements from index 0 to 2
# print(numArray.sumRange(2, 5))  # Sum of elements from index 2 to 5
# print(numArray.sumRange(0, 5))  # Sum of elements from index 0 to 5

# leetcode 525 didnt understand
# class Solution(object):
#     def findMaxLength(self, nums):
#         # Transform the array: 0 -> -1 and 1 remains 1
#         transformed = [-1 if x == 0 else 1 for x in nums]
        
#         # Dictionary to store the first occurrence of each prefix sum
#         prefix_sum_map = {0: -1}  # Initial prefix sum of 0 before any element is considered
#         prefix_sum = 0
#         max_length = 0
        
#         # Iterate through the transformed array
#         for i, num in enumerate(transformed):
#             # Update the prefix sum
#             prefix_sum += num
            
#             # Check if this prefix sum has been seen before
#             if prefix_sum in prefix_sum_map:
#                 # Calculate the length of the subarray with sum 0
#                 length = i - prefix_sum_map[prefix_sum]
#                 # Update the maximum length found
#                 max_length = max(max_length, length)
#             else:
#                 # Store the first occurrence of this prefix sum
#                 prefix_sum_map[prefix_sum] = i
        
#         return max_length

# # Example usage
# solution = Solution()
# nums = [0, 1, 0, 1]
# print(solution.findMaxLength(nums))  # Output: 4

# own testing
# nums = [2,3,3,4,5,6,7,8,9,10]
# prefix = 0
# for i, num in enumerate(nums):
#     prefix += num
#     print(prefix)        


#Leetcode 560 hier musst du die dictionary verstehen

# class Solution(object):
#     def subarraySum(self, nums, k):
#         prefix_sum = 0  # To keep track of the running total
#         prefix_sum_map = {0: 1}  # To handle the case when the subarray sum itself is k
#         count = 0  # To count the number of subarrays that sum to k
        
#         for num in nums:
#             prefix_sum += num  # Update the running total
            
#             # Check if there is a prefix sum that would result in a subarray sum of k
#             if (prefix_sum - k) in prefix_sum_map:
#                 count += prefix_sum_map[prefix_sum - k]
            
#             # Update the hash map with the current prefix sum
#             if prefix_sum in prefix_sum_map:
#                 prefix_sum_map[prefix_sum] += 1
#             else:
#                 prefix_sum_map[prefix_sum] = 1
        
#         return count

# # Example usage
# solution = Solution()
# nums = [1, 1, 1]
# k = 2
# print(solution.subarraySum(nums, k))  # Output: 2

