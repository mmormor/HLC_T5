def check_pass():

    system_pass='secreta123'
    tries=0
    while tries < 0:
        user_pass=input('Introduce tu contraseña ')

        if(user_pass==system_pass):
            print('Bienvenido')
            break
        else:
            tries=tries+1
            if tries < 3:
                print('Incorrecto, te quedan ',tries,' restantes')
            else:
                print('!Cuenta bloqueada¡')        





