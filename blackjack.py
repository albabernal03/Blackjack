from random import choice, sample

cartas = {
chr(0x1f0a1): 11,
chr(0x1f0a2): 2,
chr(0x1f03): 3,
chr(0x1f04): 4,
chr(0x1f05): 5,
chr(0x1f06): 6,
chr(0x1f07): 7,
chr(0x1f08): 8,
chr(0x1f09): 9,
chr(0x1f0aa): 10,
chr(0x1f0ab): 10,
chr(0x1f0ad): 10,
chr(0x1f0ae): 10,
}

# Añado un print para que lea las cartas y la muestre por la terminal de salida 

print("Cartas: {}".format(" ".join(cartas.keys())))
print("Puntos: {}".format(list(cartas.values())))




