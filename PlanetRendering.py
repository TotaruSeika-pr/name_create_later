from Rendering import Rendering
import time

def PlanetRendering():
    a = True
    planet_map = Rendering.PlanetMap()

    key = int(input('-> '))

    while a:
        planet_map.Clear()
        planet_map.MapDraw(key)
        time.sleep(1)

PlanetRendering()