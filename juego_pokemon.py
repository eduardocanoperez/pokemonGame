#proyecto juego pokemon.

class Pokebolas:

    def __init__(self, cantidad, tipo):
        self.cantidad = cantidad
        self.tipo = tipo

        print(f'tienes {cantidad} pokeballs {tipo}')

class Pokemones:

    def __init__(self, tipo, poder, devilidad):
        self.tipo = tipo
        self.poder = poder
        self.devilidad = devilidad

        print(f'tu pokemon es Pikachu es {tipo} con poder {poder}devil contra {devilidad}')

class Jugador:

    def __init__(self, nombre):
        self.nombre = nombre

        print(f'Hola {nombre} lista para la batalla?')
class Contrincante:

    def __init__(self, nombre):
        self.nombre = nombre
        print(f'listo para la batalla?')


class Juego:
    def __init__(self):
        pass

if __name__ == '__main__':
    jugador1 = Jugador
    jugador1('mary')