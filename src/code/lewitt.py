
# Sol Lewitt inspired work.

import random

import rhinoscriptsyntax as rs



def random_connections(width, height, points):
    """
    WALL DRAWING
    BOSTON MUSEUM

    On a wall surface, any
    continuous stretch of wall,
    using a hard pencil, place
    fifty points at random.
    The points should be evenly
    distributed over the area 
    of the wall. All of the
    points should be connected
    by straight lines.
    """

    px = []

    for i in range(points):
        x = random.uniform(0, width)
        y = random.uniform(0, height)
        px.append((x, y, 0))

    lines = []

    for i, p in enumerate(px):
        connections = px[i+1:]
        for c in connections:
            line = (p, c)
            lines.append(line)

    for p in px:
        rs.AddCircle(p, .5)

    for start, end in lines:
        rs.AddLine(start, end)


def wall_drawing_797(width, count, distance):
    """
    The first drafter has a black marker and makes an irregular
    horizontal line near the top of the wall. Then the second drafter
    tries to copy it (without touching it) using a red marker. The third
    drafter does the same, using a yellow marker. THe fourth drafter
    does the same, using a blue marker. Then the second drafter,
    followed by the third and fourth, copies the last line drawn until
    the bottom of the wall is reached.
    """
    # How to simulate a hand-drawn line?
    
    
def wall_drawing_273(grid_size):
    """
    7. Wall Drawing #273: Lines to points on a grid. A six-inch (15 cm) grid covering the wall. 
    Lines from the corners, sides, and center of the walls to random points on the grid. 
    Composite (seventh wall): red lines from the midpoints of four sides, 
      blue lines from four corners, yellow lines from the center. 
    1975
    """

    grid_points = []

    for i in range(grid_size):
        for j in range(grid_size):
            grid_points.append((i, j))

    end = grid_size - 1
    midpoint = grid_size / 2
    origins = [
        (0, 0), (0, midpoint), (0, end),
        (midpoint, 0), (end, 0),
        (midpoint, end), (end, midpoint), 
        (end, end), (midpoint, midpoint)
        ]

    lines = []

    for origin in origins:
        for e in range(10):
            terminus = select_grid_point(grid_points, (0, end))
            lines.append((origin, terminus))

    lx = []

    for start, end in lines:
        s2 = (start[0], start[1], 0)
        e2 = (end[0], end[1], 0)
        lx.append(rs.AddLine(s2, e2))
        #print(start)
        #print(end)

    g = rs.AddGroup(lx)
    return g


    #print(lines)

    """
    for line in lines:
        x0, y0 = lines[0]
        x1, y1 = lines[1]
        p0 = (x0, y0, 0)
        p1 = (x1, y1, 0)
        print(p0, p1)
        #rs.AddLine(p0, p1)
    """



def select_grid_point(grid_points, exclude):
    while True:
        candidate = random.choice(grid_points)
        if candidate[0] not in exclude and candidate[1] not in exclude:
            return candidate
            

if __name__ == "__main__":
    #random_connections(80, 80, 50)

    wall_drawing_273(16)

    #units = 16
    #for e in range(20):
    #    wall_drawing_273(16)
    
        


    
