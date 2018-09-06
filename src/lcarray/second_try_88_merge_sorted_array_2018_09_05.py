"""
The mistake I was doing:

Not understanding what in-place means


"""

"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        idx1 = m -1
        idx2 = n -1
        lastidx = m+n -1 # This is which will shrink as we move
        # Now the loop shall only compare (m-1) elements with (n-1) elements
        while (idx2 >= 0):
          # we start with last element
          #possibility 1. Last element of nums1 is bigger than last element of nums2
          print("entering loop nums1 {}".format(nums1))
          if idx2 >=0:
            if nums2[idx2] > nums1[idx1]:
              nums1[lastidx] = nums2[idx2]
              idx2 -= 1
              print("small array value greater than big array {}".format(nums1))
            else:
              nums1[lastidx] = nums1[idx1]
              idx1 -= 1
              print("else  {}".format(nums1))
          lastidx -= 1


if __name__ == "__main__":
  nums1 = [1,2,3,0,0,0]
  Solution().merge(nums1, 3, [2,5,6], 3)
  print(nums1)