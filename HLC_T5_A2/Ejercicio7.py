def fibonacci():
        a=0
        b=1
        for i in range(100):
                print(a)
                # a,b=b,a+b forma mas facil
                c=a+b
                a=b
                b=c


fibonacci()


