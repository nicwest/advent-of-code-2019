import fileinput


class Body:

    def __init__(self, name):
        self.name = name
        self.sats = []

    def orbits(self, i=0):
        return i + sum(sat.orbits(i + 1) for sat in self.sats)

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

    print(bodies['COM'].orbits())
