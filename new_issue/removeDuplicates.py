class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        slow = 1
        for index in range(1,len(nums)):
            if nums[index] != nums[index-1]:
                nums[slow] = nums[index]
                slow += 1
        return slow

if __name__ == "__main__":
    test_list = [0,0,1,1,1,2,2,3,3,4,4]
    sol = Solution()
    new_length = sol.removeDuplicates(test_list)
    print new_length,test_list[:new_length]