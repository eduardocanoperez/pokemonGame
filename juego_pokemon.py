#proyecto juego pokemon.

class Jugador:

    def __init__(self, nombre):
        self.nombre = nombre


class Pokemones:

    def __init__(self, nombre, tipo, poder, vida, ataque):
        self.nombre = nombre
        self.tipo = tipo
        self.poder = poder
        self.vida = vida
        self.ataque = ataque

    def mensaje(self):      
        print(f'{self.nombre} de tipo {self.tipo}, nivel de ataque {self.poder}, vida {self.vida}, ataque {self.ataque}.')
        
'''def main():
    while True:
        pass'''

if __name__ == '__main__':
    pokemon1 = Pokemones('Pikachu', 'Electrico', poder=8, vida=10, ataque=6)
    pokemon1.mensaje()