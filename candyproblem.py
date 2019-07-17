a = int(input())
l = list(map(int, input().split()))
l.sort()
sum = 1
count = 1
for i in range (1,len(l)):
	check = l[i-1]
	if l[i]==check:
		sum += count
	if l[i] != check:
		count += 1
		sum += count
print (sum)
