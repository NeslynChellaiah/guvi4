class main():
    def func(self):
        x,y = input().split()
        a = abs(len(x)-len(y))
        count = 0
        if len(x) > len(y):
            if y in x:
                count = a
        else:
            y = y[:len(x)]
            for i in range (len(x)):
                if x[i] != y[i]:
                    count += 1
            count = count + a
        print (count)

ob = main()
ob.func()
