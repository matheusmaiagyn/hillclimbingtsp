import random
import numpy as np

class cv(object):
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self):
        self.Dimension = 0
        self.node = []
        self.adj_matrix = [[]]
        self.path = None

        self.read_file('dantzig42.tsp')
        self.calc_euc(self.node)
        self.total = self.tot_distance()

    def read_file(self, name):
        file = open('Places/' + name)

        file.readline()
        file.readline()
        file.readline()
        self.Dimension = int(file.readline().strip().split()[2])  # DIMENSION
        file.readline()
        file.readline()

        for i in range(0, self.Dimension):
            coord = file.readline().strip().split()[1:]
            self.node.append(coord)

    def calc_euc(self, nodes):
        self.adj_matrix = [[0 for x in range(len(nodes))] for y in range(len(nodes))]
        x = 0
        y = 0
        for city1 in nodes:
            for city2 in nodes:
                self.adj_matrix[x][y] = np.sqrt((float(city1[0]) - float(city2[0]))**2 + (float(city1[1]) - float(city2[1]))**2)
                y += 1
            x += 1
            y = 0

    def create_random(self):
        node = []
        for i in range(self.Dimension):
            node.append(i)
        random.shuffle(node)
        return node

    def tot_distance(self):
        total = 0
        if self.path == None:
            self.path = self.create_random()
        for i in range(len(self.node)-1):
            #print(self.path[i], self.path[i + 1])
            total += self.adj_matrix[self.path[i]-1][self.path[i + 1]-1]
        total += self.adj_matrix[self.path[1]][self.path[0]]

        return total
