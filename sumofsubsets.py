a,b = input().split()
a = int(a)
b = int(b)
l = [int(x) for x in input().split()]
l1=[]
for i in range (0,b):
	u,v = input().split()
	u = int(u)-1
	v = int(v)
	a = l[u:v]
	sum = 0
	for i in range (0,len(a)):
		sum += a[i]
	l1.append(sum)
for i in range (0,b):
	print (l1[i])
