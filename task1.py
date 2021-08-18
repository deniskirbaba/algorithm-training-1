s = input()
ans = ''
anscnt = 0
d = {}
for ch in s:
	if ch not in d:
		d[ch] = 0
	d[ch] += 1
	if d[ch] > anscnt:
		anscnt = d[ch]
		ans = ch
print(ans)