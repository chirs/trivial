
# Create the semi-random strip image from Paul's roommate.


# https://en.wikibooks.org/wiki/Python_Imaging_Library/Editing_Pixels

from PIL import Image
import random

COLUMN_COUNT = 20
LINES = 50



def hex2tuple(hex_number):
    """
    Convert a hex number to a tuple.
    """
    s = str(hex_number)
    if s.startswith("#"):
        s = s[1:]

    return tuple([int(s[x*2:x*2+2], 16) for x in range(3)])


def tuple2hex(tup):
    a, b, c = [hex(e)[2:].zfill(2) for e in tup]
    s = a + b + c
    return s
    


def select_length():
    """
    No idea
    """
    return random.choice(range(5, 20))

def select_colors(colors, count):
    """
    Select colors from a list of colors.
    """
    l = []
    for e in range(count):
        l.append(random.choice(colors))
        
    return l



def generate_lengths(length, rng):
    """
    Generate a list of numbers within a range that adds up to a given length.
    """
    # Last number may not be in range.

    if type(rng) == tuple:
        minimum, maximum = rng
    else:
        minimum = 1
        maximum = rng

    lengths = []
    distance = 0

    while distance < length:
        l = random.randint(minimum, maximum)

        distance += l
        if distance > length:
            diff = distance - length
            l = l - diff

        lengths.append(l)

    return lengths


def make_color_list(lengths, colors):
    l = []
    for item, color in zip(lengths, colors):
        cells = [color] * item
        l.extend(cells)
    return l

            
def pauls_house(dimensions, dst, colors):
    """
    An art board like at Paul's house
    """
    x, y = dimensions

    image = Image.new( 'RGB', dimensions, "black") # create a new black image

    row_lengths = generate_lengths(y, (4, 12))
    column_lengths = generate_lengths(x, (1, 120))

    y0 = 0

    for length in row_lengths:
        column_colors = [hex2tuple(random.choice(colors)) for e in column_lengths]
        color_list = make_color_list(column_lengths, column_colors)
        for y in range(y0, y0 + length):
            for x, color in enumerate(color_list):
                px = image.putpixel((x,y), color)

        y0 += length
        

    image.save(dst)




def random_colors(dimensions, dst, colors):
    """
    Random colors for the given dimensions.
    """

    image = Image.new("RGB", dimensions, "white")

    x, y = dimensions
    for e in range(x):
        for f in range(y):
            color = hex2tuple(random.choice(colors))
            px = image.putpixel((e, f), color)

    image.save(dst)
            


def main():
    """
    Run the program.
    """

    COLORS = [
        #("000000"),
        "cccccc",
        "ffffff",
        "ff0000",
        "339933",
        "ffff00",
        ]

    colors2 = [
        "cccccc",
        "ffffff",
        "ff0000",
        "339933",
        "ffff00",
        "ff3300",
        "993300",
        "993399",
        ]


    colors3 = []
    for e in range(100):
        r = int(255 * random.random())
        g = int(255 * random.random())
        b = int(255 * random.random())
        colors3.append(tuple2hex((r, g, b)))


    dimensions = (2000, 800)
    #random_colors(dimensions, 'img2.gif', COLORS)
    #random_colors(dimensions, 'img4.gif', colors2)
    random_colors(dimensions, 'img5.gif', colors3)
    #pauls_house(dimensions, 'img3.gif', COLORS)



if __name__ == "__main__":
    """
    Simple main script
    """
    main()

        
        
    

        

