def fib(n):
	f_0=0
	f_1=1
	for i in range(n):
		f=f_0+f_1
		f_0=f_1
		f_1=f
		print(f)
	return f

print(fib(6))

def fib_(n):
	f_0=0
	f_1=1
	k=[]
	for i in range(n):
		f=f_0+f_1
		k.append(f)
		f_0=f_1
		f_1=f
	return f, k
print(fib_(100))