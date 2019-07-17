l = []
a,b = input().split()
b = int(b)
l1 = list(map(int,input().split()))

for i in range (0,len(l1)-1):
	for j in range (i+1,len(l1)):
		sum1 = l1[i]+l1[j]
		l.append(sum1)
if b in l:
	print ('yes')
else:
	print ('no')
