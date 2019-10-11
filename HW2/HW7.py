def get_three_sum(nums, target):
    for i in range(len(nums) - 2):
        for x in range(i + 1, len(nums) - 1):
            for z in range(x + 1, len(nums)):
                if nums[i] + nums[x] + nums[z] == target:
                    return i, x, z
            return None
if __name__ == "__main__":
    print(get_three_sum([2, 7, 11, 15], 24))