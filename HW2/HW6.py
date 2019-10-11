def get_two_sum(nums, target):
    for i in range(len(nums) - 1):
        for x in range(i + 1, len(nums)):
            if nums[i] + nums[x] == target:
                return i, x
        return None
if __name__ == "__main__":
    print(get_two_sum([2, 7, 11, 15], 9))