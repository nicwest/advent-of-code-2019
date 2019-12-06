import fileinput
import math


class Body:

    def __init__(self, name, distance=math.inf):
        self.name = name
        self.orbits = None
        self.sats = []
        self.distance = distance

    def set_distance(self, last=None, d=0):
        self.distance = d
        for sat in self.sats:
            if sat is not last:
                sat.set_distance(last=self, d=d + 1)
        if self.orbits and self.orbits is not last:
            self.orbits.set_distance(last=self, d=d + 1)

    def shortest(self, transfers=0):
        if self.distance == 1:
            return transfers - 1
        if not self.orbits:
            self.orbits = Body()
        return sorted(
            self.sats + [self.orbits],
            key=lambda x: x.distance
        )[0].shortest(transfers=transfers + 1)

    def __repr__(self):
        return self.name


if __name__ == '__main__':
    bodies = {}

    for orbit in fileinput.input():
        a, b = orbit.strip().split(')')
        if a not in bodies:
            bodies[a] = Body(a)
        if b not in bodies:
            bodies[b] = Body(b)
        bodies[a].sats.append(bodies[b])
        bodies[b].orbits = bodies[a]

    bodies['SAN'].set_distance()
    print(bodies['YOU'].shortest())
