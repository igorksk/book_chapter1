def odd_sum(nums):

    odds = [k for k in nums if k%2==1]

    return sum(odds)

print(odd_sum([5,10,1,60,25,3]))