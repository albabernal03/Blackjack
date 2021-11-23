# Blackjack

Mi dirección de Githup para este repositorio es el siguiente:(https://github.com/albabernal03/Blackjack.git)

En esta tarea hemos resuleto el juego del Blackjack de una forma muy básica, basándonos en lo que esta nos pedía:


**Obtener el valor de cada carta**.

**Hay que crear a partir de este diccionario una lista de cartas, que utilizaremos para poder escoger una carta**.

**Ahora podemos hacer escoger al jugador dos cartas, una a continuación de la otra**

**Agregar la puntuación de la carta seleccionada**

**A continuación, la banca escoge dos cartas al azar**

**Sumar los valores de ambas cartas.**


EL DIAGRAMA DE FLUJO ES EL SIGUIENTE:

![DIAGRAMA DE FLUJO](https://user-images.githubusercontent.com/91721875/143091518-9ccc5cb9-6065-4b34-9874-08aaea1c0dc4.jpg)


```
from random import choice

cartas = {
'A': 11,
'2': 2,
'3': 3,
'4': 4,
'5': 5,
'6': 6,
'7': 7,
'8': 8,
'9': 9,
'10': 10,
'J': 10,
'Q': 10,
'K': 10,
}

listaCartas= list(cartas)

print('.::BLACK JACK.::')
print('Cartas del jugador')

carta1= choice(listaCartas)
puntuacionJug = cartas [carta1]
print('Primera cartas:', carta1)

carta2 = choice(listaCartas)
puntuacionJug += cartas[carta2]
print('Segunda carta:', carta2)

print('Puntación total del jugador:', puntuacionJug )

carta1 = choice(listaCartas)
puntuacionBanca = cartas[carta1]
print('Primera carta:', carta1)

carta2 = choice(listaCartas)
puntuacionBanca += cartas[carta2]
print('Segunda carta:', carta2)

print('Puntuación total de la banca:', puntuacionBanca)

if puntuacionJug > puntuacionBanca:
    print('Felicidades! Has ganado!')
elif puntuacionJug < puntuacionBanca:
    print('Ha ganado la banca!')
else:
    print('Han empatado!')

```
