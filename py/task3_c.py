force = []
numberlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num = int(5)

for i in numberlist:
	if i < num:
		force.append(i)
		sumf = sum(force)

print(force, "or the sum: ", sumf)
