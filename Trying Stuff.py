# from collections import Counter
#leetcode 884

# class Solution(object):
#     def uncommonFromSentences(self, s1, s2):
#         count = {}
 
#         for word in s1.split(" ") + s2.split(" "):
#             if word in count:
#                 count[word] +=1
#             else: 
#                 count[word] = 1
        
#         print(count)

#         res = []


#         for x in count:
#             if count[x] == 1:
#                 res.append(x) 
#         return res
# solution = Solution()

# print(solution.uncommonFromSentences("this apple is sweet", "this apple is sour"))
# '{'this': 2, 'apple': 2, 'is': 2, 'sweet': 1, 'sour': 1}
# ['sweet', 'sour']'



#eigner test
# s1 = 'Hallo ich bin ein großer Mensch'
# s2 = 'Hallo ich bin ein kleiner Mensch'

# count = {}
 
# for word in s1.split(' ') + s2.split(' '):
#     if word in count:
#         count[word] +=1
#     else: 
#         count[word] =0


# res = []


# for x in count:
#     if count[x] == 0:
#         res.append(x) 
 

# print(res)

#Given an two int and an array of 7 values, I want to sum the number of the array from the position given by the first array:



# def sumrange(left, right, array):
#     # Create a dictionary where key is the index and value is the array element
#     index_dictionary = {i: v for i, v in enumerate(array)}
    
#     print(index_dictionary)
#     # Sum the values in the range from left to right (inclusive)
#     res = sum(index_dictionary[i] for i in range(left, right + 1))
    
#     return res

# # Example usage
# print(sumrange(1, 3, [2, 3, 4, 5, 6])) 
# #{0: 2, 1: 3, 2: 4, 3: 5, 4: 6}
# #12


#leetcode 303
# class NumArray(object):

#     def __init__(self, nums):
#         self.prefix = []
#         cur = 0

#         for x in nums:
#             cur += x
#             self.prefix.append(cur)
        

# # nums = [2, 3, 4, 5, 6] für mich zum checken, was es macht
# # num_array = NumArray(nums)


#     def sumRange(self, left, right):
#         rightSum = self.prefix[right]
#         leftSum= self.prefix[left] if left > 0 else 0
#         return rightSum - leftSum



#GPt task
#  You are given an array nums of integers. Your task is to implement a class called RangeSum that can handle the following operations efficiently using a prefix sum approach:

# Initialize the object with the integer array nums.
# Return the sum of elements between two indices left and right, inclusive.
# Return the sum of elements up to a certain index i (inclusive).       

class RangeSum:
    def __init__(self, nums):
        count = 0
        self.prefix_sum_list = []

        for x in nums:
            count += x
            self.prefix_sum_list.append(count)

            
    
    def sumRange(self, left, right):
        sum_left = self.prefix_sum_list[left-1] if left > 0 else 0
        sum_right = self.prefix_sum_list[right]
        end_sum = sum_right - sum_left 
        return end_sum        


    
    def sumUpTo(self, i):
        sum_index = self.prefix_sum_list[i]
        return sum_index



# Initialize the object with an array of integers
range_sum = RangeSum([1, 3, 5, 7, 9, 11])

# Query the sum of elements between indices 1 and 3
print(range_sum.sumRange(1, 3))  # Output: 15 (3 + 5 + 7)

# Query the sum of elements between indices 0 and 5
print(range_sum.sumRange(0, 4))  # Output: 36 (1 + 3 + 5 + 7 + 9 + 11)

# Query the sum of elements up to index 2
print(range_sum.sumUpTo(2))  # Output: 9 (1 + 3 + 5)
















