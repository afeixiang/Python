class Time:
    """
    Represents the time of day. Test of change.

    attributes: hour, minute, second
    """

    def print_time(self):
        '''
        Print time in format: hh:mm:ss

        self: Time
        '''
        #print('{1:2d}:{}:{}'.format(time.hour, time.minute, time.second))
        print('%.2d:%0.2d:%0.2d' % (self.hour, self.minute, self.second))

    def __str__(self):
        return '%.2d:%0.2d:%0.2d' % (self.hour, self.minute, self.second)

    def time_to_int(self):
        '''
        Convert time to intger.

        self: Time
        '''
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self, seconds):
        '''
        Add seconds to current time.

        self: Time
        seconds: integer
        '''
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        '''
        Return true if time1 is after time2 or false if not

        self: Time
        other: Time
        '''
        second1 = self.second + (self.minute + self.hour * 60) * 60
        second2 = other.second + (other.minute + other.hour * 60) * 60
        result = second1 > second2
        print(result)

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        if isinstance(other, Time):
            seconds = self.time_to_int() + other.time_to_int()
            return int_to_time(seconds)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def add_time(self, t2):
        assert valid_time(self) and valid_time(t2)
        seconds = self.time_to_int() + t2.time_to_int()
        return int_to_time(seconds)

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time



def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def main():
    time = Time()
    time.hour = 2
    time.minute = 59
    time.second = 3

    time2 = Time()
    time2.hour = 1
    time2.minute = 9
    time2.second = 30
    Time.print_time(time)
    time2.print_time()
    Time.print_time(time + time2)
    time.is_after(time2)

def main2():
    time = Time(1,52)
    print('Time1:')
    time.print_time()
    print('Time2:')
    time2 = Time(8,9,45)
    time2.print_time()
    print('Add:')
    print(time + time2)
    print('Add int: 1')
    print(time + 1)
    print(1 + time)

if __name__ == "__main__":
    main2()
