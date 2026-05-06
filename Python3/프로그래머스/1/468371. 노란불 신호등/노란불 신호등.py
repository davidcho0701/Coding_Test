def solution(signals):
	cycles = [g + y + r for g, y, r in signals]
	lcm = 1
	for c in cycles:
		a, b = lcm, c
		while b:
			a, b = b, a % b
		lcm = lcm * c // a

	for t in range(1, lcm + 1):
		x = t - 1
		all_yellow = True
		for g, y, r in signals:
			cycle = g + y + r
			pos = x % cycle
			if not (g <= pos < g + y):
				all_yellow = False
				break
		if all_yellow:
			return t
	return -1
