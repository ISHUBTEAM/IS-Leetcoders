class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, n + m) :
            nums1[i] = nums2[i - m]
        nums1.sort()
        


# other try its working but the rule is say not "Do not return anything" 

# def merge():
#     # nums1 = [1,2,3,0,0,0]
#     # m = 3
#     # nums2 = [2,5,6]
#     # n = 3 #[1,2,2,3,5,6]

#     nums1 = [1]
#     m = 1
#     nums2 = []
#     n = 0 # 1

#     new = []
#     for i in range(len(nums1)):
#         if i < m:
#             new.append(nums1[i])
    
#     for j in range(len(nums2)):
#         if j < n:
#             new.append(nums2[j])

#     new.sort()
#     nums1 = new
#     return nums1

# def merge():
#     nums1 = [1,2,3,0,0,0]
#     m = 3
#     nums2 = [2,5,6]
#     n = 3 #[1,2,2,3,5,6]

#     # nums1.remove(nums1[m:])
            
    
#     # for j in range(len(nums2)):
#     #     if j < n:
#     #         new.append(nums2[j])

#     # a = nums1[:m] + nums2[:n]
#     # a.sort()
#     nums1.insert(0, nums1[:m] + nums2[:n])
#     return nums1