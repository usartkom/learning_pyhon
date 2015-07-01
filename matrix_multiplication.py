'''
	You can find the wrong multiplication version of two matrices here:
		http://pymbook.readthedocs.org/en/latest/datastructure.html
	I changed the code and now it works right!
'''

n = int(raw_input("Enter the value of n: "))
print("Enter values for the Matrix A")
a = []
for i in range(0, n):
    a.append([int(x) for x in raw_input("").split(" ")])
print("Enter values for the Matrix B")
b = []
for i in range(0, n):
    b.append([int(x) for x in raw_input("").split(" ")])
c = []
for i in range(0, n):
	c.append([])
	for k in range(0, n):
		c[i].append(sum([a[i][j] * b[j][k] for j in range(0,n)])) 
print("After matrix multiplication")
print("-" * 10 * n)
for x in c:
    for y in x:
        print "%5d" % y,
    print("")
print("-" * 10 * n)