import random
nums = random.sample(range(100), 10)

odd = 0
even = 0

for n in nums:
    if n % 2 == 0:
       even += 1
    else:
        odd += 1

print("Odd:", odd, "- Even:", even)
print(nums)