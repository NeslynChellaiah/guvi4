k = int(input())
l = []
main = []
for i in range (0,k):
	l = list(map(int,input().split()))
	for i in range (0,len(l)):
		main.append(l[i])
	del(l)
main.sort()
for i in range (0,len(main)-1):
	print (main[i],end=" ")
print (main[-1],end="")
