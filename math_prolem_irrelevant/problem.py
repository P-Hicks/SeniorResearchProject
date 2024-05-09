
total = 0
count = 0

for a in range(4):
	print(a)
	for b in range(4):
		for c in range(4):
			for d in range(4):
				for e in range(4):
					if len({a,b,c,d,e}) == 3:
						count = count + 1
					total = total + 1

print(f"{count} / {total}")
