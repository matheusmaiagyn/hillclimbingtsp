import time

import cv

class sa(object):
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self):
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
            if self.current.total < n.total:
                bestNeighbour = n
        return bestNeighbour

    def getNeighbours(self, solution):
        neighbour = cv.cv()
        neighbours = []
        for i in range(len(solution.path)):
            for j in range(i + 1, len(solution.path)):
                neighbour.path = solution.path.copy()
                neighbour.path[i] = solution.path[j]
                neighbour.path[j] = solution.path[i]
                neighbours.append(neighbour)

        for i in range(len(neighbours)):
            neighbours[i].tot_distance()

        return neighbours

sa()