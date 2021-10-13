from PIL import Image

image = Image.open("C:/PythonFiles/stuff.png")
image.show()

print(f"Format: {image.format}, size: {image.size}, mode: {image.mode}")
size = image.size
mode = image.mode
format = image.format


pixels = image.load()
"""red_image = Image.new(mode, size)
red_pixels = red_image.load()
grey_image = Image.new(mode, size)
grey_pixels = grey_image.load()
inverted_image = Image.new(mode, size)
inverted_pixels = inverted_image.load()
weighted_grey_scale_image = Image.new(mode, size)
weighted_pixels = weighted_grey_scale_image.load()

for y in range(size[1]):
    for x in range(size[0]):
        pixel = pixels[x, y]
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]
        grey_scale = int((red + green + blue)/3)
        weighted_grey_scale = int(0.299 * red + 0.587 * green + 0.114 * blue)
        red_pixels[x, y] = (red, 0, 0)
        grey_pixels[x, y] = (grey_scale, grey_scale, grey_scale)
        inverted_pixels[size[0]-x-1, y] = (red, green, blue)
        weighted_pixels[x, y] = (weighted_grey_scale, weighted_grey_scale, weighted_grey_scale)


red_image.show()
grey_image.show()
inverted_image.show()
weighted_grey_scale_image.show()"""


outline_image = Image.new(mode, size)
outline_pixels = outline_image.load()

for y in range(size[1]-1):
    for x in range(size[0]-1):
        pixel = pixels[x, y]
        neighbour_pixels = [pixels[x+1, y+1], pixels[x+1, y-1], pixels[x-1, y+1], pixels[x-1, y-1]]
        colour_list = []
        for p in range(len(neighbour_pixels)):
            new_colour = []
            for i in range(4):
                colour = pixel[i] - neighbour_pixels[p][i]
                if colour < 0:
                    colour = -colour
                new_colour.append(colour)
            colour_list.append(new_colour)
        new_pixel = []
        for i in range(4):
            new_pixel.append(int((colour_list[0][i] + colour_list[1][i] + colour_list[2][i] + colour_list[3][i])/4))
        outline_pixels[x, y] = tuple(new_pixel)

outline_image.show()

"""
Looks good. It doesn't run for me because you've used a file that is in a different folder.

You can assign tuples in one line so lines 22 to 25 could be replaced with:
red, green, blue = pixels[x,y][0:3]

"""
