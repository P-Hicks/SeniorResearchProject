
import random
from operator import countOf
total = 0
chance = 0
i = 0
while True:
	count = [0,0,0,0]	
	roll = [random.randint(1,4) for i in range(5)]
	for num in roll:
		count[num-1] = 1 + count[num-1]
	l_c = countOf(count, 0)
	# assert sum(count) == 5
	if l_c == 1:
		chance = 1 + chance
	total = 1 + total
	i = (i + 1) % 100000
	if (i == 0):
		print(str(roll) + " : " + str(l_c) + " : " + str(chance) + "/" + str(total)+  " : " +  " : " + str(chance / total))
	


