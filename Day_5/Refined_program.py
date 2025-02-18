rules, updates = open('input.txt').read().split('\n\n')
updates = [x.split(',') for x in updates.split('\n')]

def order(nums): 
    return sorted(nums, key=lambda x: -sum(f"{x}|{y}" in rules for y in nums))

print(sum(int(order(nums)[len(nums)//2]) for nums in updates if order(nums) == nums))
print(sum(int(order(nums)[len(nums)//2]) for nums in updates if order(nums) != nums))