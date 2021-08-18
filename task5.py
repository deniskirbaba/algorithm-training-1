tnow, tgoal = map(int, input().split())
mode = input()
if mode == "fan":
	print(tnow)
elif mode == "freeze":
	if tnow > tgoal:
		print(tgoal)
	else:
		print(tnow)
elif mode == "heat":
	if tnow < tgoal:
		print(tgoal)
	else:
		print(tnow)
else:
	print(tgoal)