k1, m, k2, p2, n2 = map(int, input().split())

if k1 == k2:
	print(int(p2), int(n2))

elif p2 == 1 and n2 == 1:
	if k1 < k2:
		print(int(p2), int(n2))
	else:
		p1 = 0
		if m == 1:
			n1 = 1
			print(int(p1), int(n1))
		else:
			n1 = 0
			print(int(p1), int(n1))
else:

	c1 = k2 / (m * (p2 - 1) + n2)
	c2 = (k2 - 1) / (m * (p2 - 1) + n2 - 1)
	print(c1, c2)

	if c1 % 1 != 0:
		c1 = c1 // 1 + 1
	c1 = int(c1)
	c2 = int(c2)

	if c1 > c2:
		p1 = n1 = -1
		print(int(p1), int(n1))

	elif c1 == c2:

		p1 = k1 / (c1 * m)
		if p1 % 1 != 0:
			p1 = p1 // 1 + 1

		n1 = (k1 - (p1 - 1) * m * c1) / c1
		if n1 % 1 != 0:
			n1 = n1 // 1 + 1

		print(int(p1), int(n1))

	else:

		dictc = {}
		isEqual = True

		qqq = k1 / (c1 * m)
		if qqq % 1 != 0:
				qqq = qqq // 1 + 1

		for i in range(c2 - c1 + 1):
			res = k1 / ((c1 + i) * m)
			if res % 1 != 0:
				res = res // 1 + 1
			if res != qqq:
				isEqual = False
			dictc[c1 + i] = res

		if not isEqual:

			isEqualN = True
			n1 = 0
			p1 = 0

			ppp = (k1 - (dictc[c1] - 1) * m * c1) / c1
			if ppp % 1 != 0:
					ppp = ppp // 1 + 1
			for i in range(c2 - c1 + 1):
				res = (k1 - (dictc[c1 + i] - 1) * m * (c1 + i)) / (c1 + i)
				if res % 1 != 0:
					res = res // 1 + 1
				if res != ppp:
					isEqualN = False

			if not isEqualN:
				print(int(p1), int(n1))
			else:
				print(int(p1), int(ppp))

		else:

			p1 = dictc[c1]
			n1 = (k1 - (p1 - 1) * m * c1) / c1
			if n1 % 1 != 0:
				n1 = n1 // 1 + 1
			print(int(p1), int(n1))