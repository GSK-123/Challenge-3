class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None
        """
        
        last_nums1 = m - 1  
        last_nums2 = n - 1  
        merge_index = m + n - 1  

        while last_nums1 >= 0 and last_nums2 >= 0:
            if nums1[last_nums1] > nums2[last_nums2]:
                nums1[merge_index] = nums1[last_nums1]
                last_nums1 -= 1
            else:
                nums1[merge_index] = nums2[last_nums2]
                last_nums2 -= 1
            merge_index -= 1

        while last_nums2 >= 0:
            nums1[merge_index] = nums2[last_nums2]
            last_nums2 -= 1
            merge_index -= 1

