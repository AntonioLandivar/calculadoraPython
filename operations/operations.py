print(f'''                 
###Bienvenido###

1. Sumar
2. Restar
3. Multiplicar
4. Dividir               
''')

opcion = int(input('Elija una opcion: '))

if opcion == 1:
    print('Programa Suma')
    a = int(input('Ingrese un numero: '))
    b = int(input('Ingrese un numero: '))
    c = a + b
    print(f'''La suma es: {c}
          
Gracias
          ''')
else:
    print('Fin de la prueba')
    