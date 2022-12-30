import random

ShipClasses = ('Destroyer', 'Cruiser', 'Merchant Vessel', 'Transport')
Allegiances = ('USA', 'UK', 'Germany', 'Sweden')

Ships = {
        'USA': {
            'Destroyer': [ 'USS Pillsbury', 'USS Flaherty',
                           'USS Chatelain', 'USS Jenks' ],
            'Cruiser': [ 'USS Wichita', 'USS Brooklyn',
                         'USS Philadelphia', 'USS Savannah',
                         'USS Nashville' ],
            'Merchant Vessel': [ 'Victory Ship' ],
            'Transport': [ 'Transport Vessel' ],
        },
        'UK': {
            'Destroyer': [ 'HMS Amazon' ],
            'Cruiser': [ 'HMS Berwick' ],
            'Merchant Vessel': [ 'Merchant Vessel' ],
            'Transport': [ 'Transport Vessel' ],
        },
        'Germany': {
            'Destroyer': [ 'Z16 Friedrich Eckoldt', 'Z7 Hermann Schoemann',
                           'Z8 Bruno Heinemann' ],
            'Cruiser': [ 'Lutzow', 'Admiral Scheer', 'Admiral Hipper' ],
            'Merchant Vessel': [ 'Merchant Vessel' ],
            'Transport': [ 'Transport Vessel' ],
        },
        'Sweden': {
            'Destroyer': [ 'Swedish Destroyer' ],
            'Cruiser': [ 'Swedish Cruiser' ],
            'Merchant Vessel': [ 'Swedish Merchant Vessel' ],
            'Transport': [ 'Swedish Cruiser' ],
        },
}

class Ship:
    def __init__(self, x, y, name=None, sclass=None, allegiance=None):
        self.x = x
        self.y = y

        if name == None and sclass == None and allegiance == None:
            self.generate()
            return

        self.name = name
        self.model = model
        self.allegiance = allegiance

    def generate(self):
        self.model = random.choice(ShipClasses)
        self.allegiance = random.choice(Allegiances)
        self.name = random.choice(Ships[self.allegiance][self.model])
