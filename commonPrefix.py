class main():
    def func(self):
        N = int(input())
        l = []
        for i in range (0,N):
            l.append(input())
        minl = len(min(l,key = len))
        for i in range (0,len(l)-1):
            for j in range (0,minl):
                if l[i][:j+1] in l[i+1]:
                    a = l[i][:j+1]
        print (a)
ob = main();
ob.func()
