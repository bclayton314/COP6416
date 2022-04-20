class Location:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id


class LocationMap:
    def __init__(self, LocationList):
        self.LocMap = {}
        for loc in LocationList:
           self.LocMap[Location.id] = Location