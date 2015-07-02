k = 0
with open('/proc/cpuinfo') as f:
	for line in f:
		if line.find('processor') != -1: 
			k += 1
print k