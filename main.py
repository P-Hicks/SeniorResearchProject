import random 
import time
start_time = time.time()
for i in range(50):
	cards = list(range(1,61))
	random.shuffle(cards)
print(time.time() - start_time)

