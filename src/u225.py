import ship
import gmap

game_map = gmap.GameMap(500, 500)
game_map.generate_ships(5)
game_map.print_map()
