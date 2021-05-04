import time

import cv

class sa(object):
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self):
        self.neighboursNum = 5

        self.current = cv.cv()
        self.neighbours = self.getNeighbours(self.current)
        self.best = self.getBestNeighbour()

        initial = time.time()

        while self.best.total < self.current.total:
            self.current = self.best
            self.neighbours = self.getNeighbours(self.current)
            self.best = self.getBestNeighbour()
            print(self.current.total)

        print(self.current.total)
        print(self.current.path)
        print(time.time() - initial)

    def getBestNeighbour(self):
        bestNeighbour = self.neighbours[0]
        for n in self.neighbours:
            if self.current.total < bestNeighbour.total:
                bestNeighbour = n
        return bestNeighbour

    def getNeighbours(self, solution):
        neighbour = cv.cv()
        neighbours = []
        for i in range(self.neighboursNum):
            for j in range(i + 1, len(solution.path)):
                neighbour.path = solution.path.copy()
                neighbour.path[i] = solution.path[j]
                neighbour.path[j] = solution.path[i]
                neighbour.tot_distance()
                neighbours.append(neighbour)
                neighbour = cv.cv()

        return neighbours

sa()
