# hold current objects and track speed
class trackobjects:

    # create  image tracker
    def __init__(self, dimensions):
        self.current_objects = {}
        self.speed = 0
        self.uid = 0

    # add object to current objects
    def add(self, coordinates):
        object_uid = self.existing_object(coordinates)
        if object_uid < 0:
            self.current_objects[self.uid] = []
            self.current_objects[self.uid].append(coordinates)
            self.uid += 1
        else:
            self.current_objects[object_uid].append(coordinates)

    # check if coordinates are similar to existing object
    def existing_object(self, coordinates):
        return -1

    # report current speed
    def report(self):
        print("Estimated speed: " + str(self.speed), '\n')