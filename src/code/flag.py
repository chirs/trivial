
# Create the semi-random strip image from Paul's roommate.


# https://en.wikibooks.org/wiki/Python_Imaging_Library/Editing_Pixels

from PIL import Image
import random

COLUMN_COUNT = 20
LINES = 50

COLORS = [
    #("000000"),
    ("cccccc"),
    ("ffffff"),
    ("ff0000"),
    ("339933"),
    ("ffff00"),
    ]


def hex2tuple(hex_number):
    """
    Convert a hex number to a tuple.
    """
    s = str(hex_number)
    if s.startswith("#"):
        s = s[1:]

    return tuple([int(s[x*2:x*2+2], 16) for x in range(3)])


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

            
def pauls_house(dimensions, dst):
    """
    An art board like at Paul's house
    """
    x, y = dimensions

    image = Image.new( 'RGB', dimensions, "black") # create a new black image

    row_lengths = generate_lengths(y, (4, 12))
    column_lengths = generate_lengths(x, (1, 120))

    y0 = 0

    for length in row_lengths:
        column_colors = [hex2tuple(random.choice(COLORS)) for e in column_lengths]
        color_list = make_color_list(column_lengths, column_colors)
        for y in range(y0, y0 + length):
            for x, color in enumerate(color_list):
                px = image.putpixel((x,y), color)

        y0 += length
        

    image.save(dst)




def random_colors(dimensions, dst):
    """
    Random colors for the given dimensions.
    """

    image = Image.new("RGB", dimensions, "white")

    x, y = dimensions
    for e in range(x):
        for f in range(y):
            color = hex2tuple(random.choice(COLORS))
            px = image.putpixel((e, f), color)

    image.save(dst)
            


def main():
    """
    Run the program.
    """

    dimensions = (2000, 800)
    #random_colors(dimensions, img2.gif)
    print(pauls_house(dimensions, 'img3.gif'))



if __name__ == "__main__":
    """
    Simple main script
    """
    main()

        
        
    

        

