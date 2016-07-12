


class CubeOld(object):
    """
    Exploring the possible permutations of a cube.
    based on Lewitt's open cube variations.
    """
    # rotations
    # http://www.euclideanspace.com/maths/discrete/groups/categorise/finite/cube/
    # 6 faces. Then which face is ...


    def __init__(self, edges=None):
        """
        Initialize a cube, or a partial cube.
        """

        if edges is None:
            self.edges = (
                (1,2), (2,3), (3,4), (4,1), 
                (1,5), (2,6), (3,7), (4,8),
                (5,6), (6,7), (7,8), (8,5),
                )
        else:
            self.edges = edges


    def __eq__(self, other):
        e1 = set(self.edges)
        e2 = set(other.edges)

        return e1 == e2


    def __hash__(self):
        return hash(tuple(sorted(self.edges)))

    @property
    def faces(self):
        """
        """
        return

    @property
    def vertices(self):
        return



    # Rotations

    def rotate(self, mapping):
        d = dict(mapping)

        new_edges = []
        for v1, v2 in self.edges:
            ne = (d[v1], d[v2])
            new_edges.append(ne)

        self.edges = new_edges

    def rotate_xz(self):
        mapping = [
            (5, 1), (6, 5), (7, 8), (8, 4),
            (1, 2), (2, 6), (3, 7), (4, 3),
                   ]
        self.rotate(mapping)
    

    def rotate_xy(self):
        mapping = [
            (1, 4), (2, 1), (3, 2), (4, 3),
            (5, 8), (6, 5), (7, 6), (8, 7),
            ]

        self.rotate(mapping)


    def rotate_yz(self):
        mapping = [
            (5, 1), (6, 2), (7, 6), (8, 5),
            (1, 4), (2, 3), (3, 7), (4, 8),
            ]

        self.rotate(mapping)



    def all_permutations(self):
        xy = self.rotate_xx
        xz = self.rotate_xz
        yz = self.rotate_yz
        


    # Edge trimming

    def remove_edge(self, edge):
        self.edges = [e for e in self.edges if e != edge]

    def remove_edges(self, edges):
        for edge in edges:
            self.remove_edge(edge)

    def remove_random_edge(self):
        import random
        e = random.choice(self.edges)
        self.remove_edge(e)



class Cube(object):
    """
    A face-based cube.
    """

    OPPOSITE_FACES = {
        1:3,
        2:4,
        3:1,
        4:2,
        5:6,
        6:5,
        }

    VERTEX_MAPPING = [
        (1, (1,4,6)),
        (2, (1,2,6)),
        (3, (2,3,6)),
        (4, (3,4,6)),
        (5, (1,4,5)),
        (6, (1,2,5)),
        (7, (2,3,5)),
        (8, (3,4,5)),
        ]


    VERTEX_DICT = dict([(b, a) for (a, b) in VERTEX_MAPPING])

    def __init__(self, faces=None):
        if faces is None:
            self.faces = [1,2,3,4,5,6] # f, r, b, l, t, b
        else:
            self.faces = faces


    @property
    def vertices(self):
        vx = []

        a, b, c, d, e, f = self.faces
        for e in [
            (a,d,f),
            (a,b,f),
            (b,c,f),
            (c,d,f),
            (a,d,e),
            (a,b,e),
            (b,c,e),
            (c,d,e),
            ]:
            key = tuple(sorted(e))
            vertex = self.VERTEX_DICT[key]
            vx.append(vertex)

        return vx


    @property
    def edges(self):
        #bottom; vertical; top
        return



    def face_neighbors(self, face):
        return [e for e in self.faces if e not in (face, self.OPPOSITE_FACES[face])]


    def clockwise_orientation(self, subfaces):
        CLOCKWISE = [
            (1,2,3,4),
            (1,6,3,5),
            (2,5,4,6),
            ]

        a, b, c, d = subfaces

        for e in [
            [a,b,c,d],
            [b,c,d,a],
            [c,d,a,b],
            [d,a,b,c]
            ]:
            if tuple(e) in CLOCKWISE:
                return True
        return False


    def construct_edge_mapping(self):
        mapping = defaultdict(list)

        for vertex, faces in self.VERTEX_MAPPING:
            f1, f2, f3 = faces
            mapping[(f1,f2)].append(vertex)
            mapping[(f2,f3)].append(vertex)
            mapping[(f1,f3)].append(vertex)

        d2 = {}
        for key, value in mapping.items():
            d2[key] = tuple(value)

        return d2


    def orientations(self):

        ol = []

        for a in self.faces:
            for b in self.face_neighbors(a):
                c = self.OPPOSITE_FACES[a]
                d = self.OPPOSITE_FACES[b]

                e, f = sorted([e for e in self.faces if e not in (a,b,c,d)]) 

                if not self.clockwise_orientation([a,b,c,d]):
                    f, e = e, f 

                orientation = [a,b,c,d,e,f]
                
                ol.append(orientation)
                
        return ol

    def get_vertex(self, faces):
        ft = tuple(sorted(faces))
        return self.VERTEX_DICT[ft]

    def get_edge(self, faces):
        return
        
    def rotate_xy(self):
        # clockwise
        f, r, b, l, t, b = self.faces
        self.faces = [r, b, l, f, t, b]


    def rotate_xz(self):
        return

    def rotate_yz(self):
        return



def is_connected(edges):
        """
        Walk an undirected graph.
        """
        # Sure forgot how to do this.

        unvisited = set([e[0] for e in edges] + [e[1] for e in edges])

        visited = set()

        to_visit = set([list(unvisited)[0]])
        # If this were a 

        while True:
            current = to_visit.pop()
            unvisited.remove(current)
            visited.add(current)

            for v1, v2 in edges:
                if v1 == current and v2 not in visited:
                    to_visit.add(v2)
                if v2 == current and v1 not in visited:
                    to_visit.add(v1)

            if len(unvisited) == 0:
                return True

            elif len(to_visit) == 0 and len(unvisited) > 0:
                return False

