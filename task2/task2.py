import sys
import math

with open(sys.argv[1], 'r') as f:
    cx, cy = map(float, f.readline().split())
    r = float(f.readline())

with open(sys.argv[2], 'r') as f:
    for line in f:
        x, y = map(float, line.split())
        # Расчет расстояния от точки до центра окружности
        dist = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
        # Определение положения точки относительно окружности
        if dist == r:
            print(0)
        elif dist < r:
            print(1)
        else:
            print(2)