
def findMedianSortedArrays(num1,num2):
    len1 = len(num1)
    len2 = len(num2)
    sum_len = len1+len2
    all_len = sorted(num1 + num2)
    if (sum_len)%2 == 0:
        mid = ((sum_len)/2-1,(sum_len/2))
        return (float(all_len[mid[0]]) + float(all_len[mid[1]]))/2
    else:
        mid = int(sum_len/2)
        return float(all_len[mid])

if __name__ == "__main__":
    nums1 = [-1,0,2,3,109]
    nums2 = [2,73,984]
    print findMedianSortedArrays(nums1,nums2)
