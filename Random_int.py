import random
dict={}
nums = [ ]
for i in range(10000):
    nums.append(random.randint(1, 10))

#count the occurence of each number in nums
unique_no=set(nums)
for i in unique_no:
    dict[i]=0

for i in nums:
    dict[i]+=1

print(dict)