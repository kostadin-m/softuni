class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hrs, mins, sec):
        self.hours = hrs
        self.minutes = mins
        self.seconds = sec

    def set_time(self, new_hours, new_min, new_sec):
        self.hours = new_hours
        self.minutes = new_min
        self.seconds = new_sec

    def get_time(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def next_second(self):
        if self.seconds + 1 > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0
        else:
            self.seconds += 1

        return self.get_time()


