class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.is_taken = False
        self.guests = 0

    def take_room(self, guests):
        if self.is_taken or guests > self.capacity:
            return f"Room number {self.number} cannot be taken"
        self.is_taken = True
        self.guests += guests
        return True


    def free_room(self):
        if not self.is_taken:
            return f"Room number {self.number} is not taken"
        self.is_taken = False
        self.guests = 0
        return True

