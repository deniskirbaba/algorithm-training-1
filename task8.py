a = int(input())
b = int(input())
c = int(input())

if c < 0:
	print("NO SOLUTION")
elif a == 0:
	if b == c**2:
		print("MANY SOLUTIONS")
	else:
		print("NO SOLUTION")
else:
	ans = (c**2 - b) / a
	if ans.is_integer():
		print(int(ans))
	else:
		print("NO SOLUTION")