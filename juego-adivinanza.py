
import random


numero_secreto = random.randint(1,100)
cantidad_intentos = 0
cantidad_intentos_max = 3
adivinado = False

print ("Bienvenido al juego de adivinar")

while not adivinado:
    if cantidad_intentos >= cantidad_intentos_max:
        print("perdiste gil")
        break
    entrada = input("introduce un número del 1 al 99: ") 
    numero = int(entrada)

    if numero == numero_secreto:
        print("Felicidades, adivinaste el número secreto")
        adivinado = True
    elif numero < numero_secreto:
        print("el número es mayor al ingresado")
    else:
        print("el número es menor al ingresado")

    cantidad_intentos += 1


    