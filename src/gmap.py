import ship, random

class GameMap:
    def __init__(self, w, h):
        self.ships = []
        self.w = w
        self.h = h

    def generate_ships(self, count):
        for i in range(count):
            self.ships.append(ship.Ship(random.randint(0, self.w), random.randint(0, self.h)))

    def print_map(self):
        for s in range(len(self.ships)):
            print('COORDS: ' + str(self.ships[s].x) + ',' + str(self.ships[s].y))
            print('NAME: ' + self.ships[s].name)
            print('TYPE: ' + self.ships[s].model)
            print('ALLEGIANCE: ' + self.ships[s].allegiance)
