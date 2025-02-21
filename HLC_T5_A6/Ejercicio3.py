def decimal_a_romano(numero):
    valores = [
        1000, 'M', 900, 'CM', 500, 'D', 400, 'CD',
        100, 'C', 90, 'XC', 50, 'L', 40, 'XL',
        10, 'X', 9, 'IX', 5, 'V', 4, 'IV', 1, 'I'
    ]
    
    resultado = ""
    for i in range(0, len(valores), 2):
        valor, simbolo = valores[i], valores[i+1]
        while numero >= valor:
            resultado += simbolo
            numero -= valor
    
    return resultado



print(decimal_a_romano(30))
