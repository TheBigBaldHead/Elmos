numbers =["1","1"]
for i in range(100):
    nextNum = str(int(numbers[-2])+int(numbers[-1]))
    numbers.append(nextNum)
#print numbers in just one line
'''
print(",".join(numbers))
'''
#print them line by line
for number in numbers:
	print(number)
