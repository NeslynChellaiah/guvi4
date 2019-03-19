class main:
    def func(self,a,b):
        b=int(b)
        print(a[b:])
a,b=input().split()
ob = main()
ob.func(a,b)
