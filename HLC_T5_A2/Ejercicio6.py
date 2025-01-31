
def check_chars():
    word=input('Introduce una palabra ')
    special_chars=['@','#','$','%']
    for char in special_chars: 
        if char in  word:
            print('La palabra  contiene el signo',char)
check_chars()
 
