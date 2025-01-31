def sum_prom():
    number=[10,20,30]
    suma=0
    
    # num_sum=sum(number)
    # total_num=len(number)
    # prom=num_sum/total_num
    # print(f'Suma:{num_sum},Promedio:{prom}')
    for i in number:
        suma=suma+i
    print('La suma es ',suma)
    print('La suma es ',suma/len(number))
sum_prom()