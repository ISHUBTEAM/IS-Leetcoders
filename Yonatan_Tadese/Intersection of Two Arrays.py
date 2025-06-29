nums1 = [4,7,9,7,6,7]
nums2 = [5,0,0,6,1,6,2,2,4] #[6,4]


def intersecting(nums1, nums2):
    one = set(nums1)
    two = set(nums2)
    result =[]
    
    for i in one:
        if i in two:
            result.append(i)
    return result

print(intersecting(nums1, nums2))