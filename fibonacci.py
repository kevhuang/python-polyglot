def fib(n):
	result = [0,1]
	if n<2:
		return n
	for x in range(2,n+1):
		sum = result[0] + result[1]
		result.pop(0)
		result.append(sum)
	return result[-1]

print(fib(8))