class main():
    def func(self):
        count = 0
        x,y = input().split()
        x = list(x)
        y = list(y)
        if len(x)<len(y):
            length1 = len(y)-1
            length2 = len(x)-1
        else:
            length2 = len(y)-1
            length1 = len(x)-1
        for i in range (length1):
            if (i <= length2):
                if x[i] != y[i]:
                    x[i] = y[i]
                    count += 1
        l = abs(len(x)-len(y))
        count += l
        print (count)


ob = main()
ob.func()
