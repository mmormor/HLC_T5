
def nota(estudiantes):

    suma_cal = 0
    mejor_estudiante = ""
    mejor_cal = 0

    for nombre, calificacion in estudiantes.items():
        suma_cal += calificacion 
        if calificacion > mejor_cal:  
            mejor_cal = calificacion
            mejor_estudiante = nombre

    promedio=suma_cal/len(estudiantes)

    return f"Promedio:{promedio:.2f}, Mejor estudiante: {mejor_estudiante} con {mejor_cal}"

estudiantes = {'Juan': 7, 'Ana': 9, 'Pedro': 6}
resultado = nota(estudiantes)
print(resultado)
