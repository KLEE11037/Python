nums = list(map(int, open('Задание 13 (1).txt').readlines()))
n = 100000
for x in nums:
    if x < n and x % 9 != 0:
        n = x
count = 0
max_sum = 0
for i in range(len(nums) - 1):
    if nums[i] % n == 0 and nums[i + 1] % n == 0:
        count += 1
        if nums[i] + nums[i + 1] > max_sum:
            max_sum = nums[i] + nums[i + 1]
print(count, max_sum)