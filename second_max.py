def second_max(nums):

    first_max = max(nums);

    nums.remove(first_max)

    return max(nums)

print(second_max([5,10,1,60,25,3]))