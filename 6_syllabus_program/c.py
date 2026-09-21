# Create a class clock having 3 init parameters – hours, minutes and seconds. Write following methods:
# a. setClock – to set the time
# b. displayTime – to show current time
# c. tick – increase the time by one second

class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def setClock(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def displayTime(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
                if self.hours == 24:
                    self.hours = 0

c = Clock(10, 15, 30)

print("Initial time:")
c.displayTime()

c.setClock(23, 59, 58)
print("\nAfter setClock(23, 59, 58):")
c.displayTime()

print("\nTicking...")
c.tick()
c.displayTime()   

c.tick()
c.displayTime()  
c.tick()
c.displayTime()   