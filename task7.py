nums = [0, 0, 0, 0]
nums[0] = input()
nums[1] = input()
nums[2] = input()
nums[3] = input()

for i in range(4):
    nums[i] = nums[i].replace('-', '').replace('(', '').replace(')', '').replace('+7', '8')
    if len(nums[i]) < 11:
        nums[i] = '8495' + nums[i]

for i in range(3):
	if nums[1+i] == nums[0]:
		print('YES')
	else:
		print('NO')