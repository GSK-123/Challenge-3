class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int lastNums1 = m - 1; 
        int lastNums2 = n - 1;  
        int mergeIndex = m + n - 1; 

        while (lastNums1 >= 0 && lastNums2 >= 0) {
            if (nums1[lastNums1] > nums2[lastNums2]) {
                nums1[mergeIndex] = nums1[lastNums1];
                lastNums1--;
            } else {
                nums1[mergeIndex] = nums2[lastNums2];
                lastNums2--;
            }
            mergeIndex--;
        }

        while (lastNums2 >= 0) {
            nums1[mergeIndex] = nums2[lastNums2];
            lastNums2--;
            mergeIndex--;
        }
    }
}
