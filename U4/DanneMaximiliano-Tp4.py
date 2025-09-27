#Ejercicio1

#i = 0
#while i <= 100:
#    print(i)
#    i += 1


##Ejercicio2

#numero = int(input("Ingrese un número entero: "))

#if numero == 0:
#    cantidad_digitos = 1
#else:
#    cantidad_digitos = 0
#    while numero > 0:
#        numero //= 10   
#        cantidad_digitos += 1

#print("El número ingresado tiene", cantidad_digitos, "dígitos.")


##Ejercicio3

#a = int(input("Ingrese el primer numero: "))
#b = int(input("Ingrese el segundo numero: "))

#menor = min(a, b)
#mayor = max(a, b)

#suma = 0

#for i in range(menor + 1, mayor):
#    suma += i

#print("La suma de los números comprendidos entre", a, "y", b, "es:", suma)

##Ejercicio4

#suma_total = 0

#print("Sumador Secuencial")
#print("Ingresa números enteros para sumarlos.")
#print("El programa se detendrá y mostrará el total cuando ingreses el número 0.")

#while True:
#    try:
#        entrada = input("\nIngresa un número (o 0 para terminar): ")
#        numero = int(entrada)

#        if numero == 0:
#            break
        
#        suma_total += numero
#        print(f"Suma actual: {suma_total}")

#    except ValueError:
#        print("¡Error! Por favor, ingresa un número entero válido.")

#print("¡Juego terminado!")
#print(f"La suma total de todos los números ingresados es: {suma_total}")


#Ejercicio 5

#import random
#numero_secreto = random.randint(0, 9)

#adivinanza = -1         
#intentos = 0             
#print("Adivina el numero entre 0 y 9")

#while adivinanza != numero_secreto:
#    intentos += 1
    
#    try:
#        adivinanza_str = input(f"\nIntento #{intentos}: Ingresa tu número: ")
#        adivinanza = int(adivinanza_str)
#    except ValueError:
#        print("Debes ingresar un número entero.")
#        intentos -= 1
#        continue 
        
#    if adivinanza < 0 or adivinanza > 9:
#        print("El número debe estar entre 0 y 9")
        
#    elif adivinanza < numero_secreto:
#        print("El número secreto es MAYOR")
        
#    elif adivinanza > numero_secreto:
#        print("El número secreto es MENOR")
        
#print("\n")
#print(f"Adivinaste el número secreto ({numero_secreto})")
#print(f"En un total de {intentos} intentos.")


#Ejercicio 6

#print("Números pares entre 100 y 0 (decreciente):")

#for numero in range(100, -1, -2):
#    print(numero)


#Ejercicio 7

#while True:
#    try:
#        limite_superior = int(input("Ingrese un número entero positivo para calcular la suma hasta ese valor: "))

#        if limite_superior < 0:
#            print("Por favor, ingrese un número que sea cero o positivo.")
#        else:
#            break 
            
#    except ValueError:
#        print("Error: Ingrese un número entero válido.")

#suma_total = 0

#for numero in range(limite_superior + 1):
#    suma_total += numero 

#print(f"La suma de todos los números enteros desde 0 hasta {limite_superior} es: {suma_total}")

#Ejercicio 8

#CANTIDAD_A_PROCESAR = 100 

#pares = 0
#impares = 0
#positivos = 0
#negativos = 0

#print(f"--- Análisis de {CANTIDAD_A_PROCESAR} Números Enteros ---")

#for i in range(CANTIDAD_A_PROCESAR):
    
#    while True:
#        try:
#            numero = int(input(f"Ingrese el número #{i + 1}: "))
#            break 
#        except ValueError:
#            print("¡Error! Debe ingresar un número entero válido.")

#    if numero > 0:
#        positivos += 1
#    elif numero < 0:
#        negativos += 1

#    if numero % 2 == 0:
#        pares += 1
#    else:
#        impares += 1

#print(f"Total de números ingresados: {CANTIDAD_A_PROCESAR}")
#print(f"Números Pares:    {pares}")
#print(f"Números Impares:  {impares}")
#print(f"Números Positivos: {positivos}")
#print(f"Números Negativos: {negativos}")

#Ejercicio 9 

#CANTIDAD_NUMEROS = 100 

#suma_total = 0

#print(f"--- Calculadora de Media de {CANTIDAD_NUMEROS} Números ---")

#for i in range(CANTIDAD_NUMEROS):
    
#    while True:
#        try:
#            numero = int(input(f"Ingrese el número entero #{i + 1}: "))
#            break 
#        except ValueError:
#            print("Error! Debe ingresar un número entero válido.")

#    suma_total += numero

# media = suma_total / CANTIDAD_NUMEROS

#print("RESULTADO")
#print(f"Suma total de los {CANTIDAD_NUMEROS} números: {suma_total}")
#print(f"La media de los valores es: {media:.2f}")


#Ejercicio 10
#numero = input("Ingresá un numero: ")
#invertido = numero[::-1]

#print("Número invertido:", invertido)