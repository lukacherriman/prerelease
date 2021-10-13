from PIL import Image, ImageDraw
import math

pi = math.pi
r = 400
res = 1000

circle = Image.new("RGB", (1000, 1000))

pixels = circle.load()

for i in range(0, r, 10):
    for j in range(res):
        x = 500 - int((i+j/100) * math.cos(2*pi/res*j))
        y = 500 + int((i+j/100) * math.sin(2*pi/res*j))
        pixels[x, y] = (int(x/4), int(y/4), 0)


lines = Image.new("RGB", (1000, 1000))
draw = ImageDraw.Draw(lines)
draw.line([(0, 0), (1000, 1000), (0, 1000), (1000, 0)], width=10, fill=(100, 125, 100))

lines.show()
