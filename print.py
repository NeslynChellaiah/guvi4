a = int(input())
l = [int(x) for x in input().split()]
l = sorted(l)
for i in range (len(l)-1,-1,-1):
	print (l[i])
