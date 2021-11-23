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



