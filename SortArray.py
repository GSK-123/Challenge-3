class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.mergeSort(nums)
    
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        
        return self.merge(left, right)
    
    def merge(self, left, right):
        sorted_array = []
        i = j = 0
        len_left = len(left)
        len_right = len(right)
        
        while i < len_left and j < len_right:
            if left[i] <= right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
        
        if i < len_left:
            sorted_array.extend(left[i:])
        if j < len_right:
            sorted_array.extend(right[j:])
        
        return sorted_array


