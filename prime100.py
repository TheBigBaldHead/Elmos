prime = []
for n in range(2,100):
	prime_check=True
	for small in range(2,n):
		if n%small == 0:
			prime_check=False
	if prime_check == True:
		prime.append(n)
print(prime)