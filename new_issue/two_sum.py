def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    new_dict = {}
    for i,item in enumerate(nums):
        if target - item in new_dict:
            return [i,new_dict[target - item]]
        new_dict[nums[i]] = i


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print twoSum(nums,target)