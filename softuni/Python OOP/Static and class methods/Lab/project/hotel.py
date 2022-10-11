class Hotel:
    def __init__(self,  name):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([x.guests for x in self.rooms])

    @classmethod
    def from_stars(cls, stars):
        return cls(f"{stars} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [x for x in self.rooms if x.number == room_number][0]
        return room.take_room(people)

    def free_room(self, room_number):
        room = [x for x in self.rooms if x.number == room_number][0]
        return room.free_room()

    def status(self):
        return f"Hotel {self.name} has {sum([self.guests])} total guests\n" \
               f"Free rooms: {', '.join([str(x.number) for x in self.rooms if not x.is_taken])}\n" \
               f"Taken rooms: {', '.join([str(x.number) for x in self.rooms if x.is_taken])}"
