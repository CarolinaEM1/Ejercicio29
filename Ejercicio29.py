# Sumar digitos de un numero entero con funcion recursiva

def sumarDigitos(num):
    if num==0:
        resultado = 0
    else: # Caso recursivo
        resultado = sumarDigitos(int(num/10)) + (num%10)

    return resultado

valor = sumarDigitos(125)


print (valor)

# Carolina EM
