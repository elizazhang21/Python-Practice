#climing ladders


num = {}
num[1] = 1
num[2] = 2
num[3] = 3
print(num)

for n in range(4,10000):
	num[n] = num[n-3] + num[n-2] + num[n-1]


print(num[11])