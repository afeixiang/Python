class Time:
    """
    Represents the time of day.

    attributes: hour, minute, second
    """

def print_time(time):
    '''
    Print time in format: hour:minute:seconds

    time: Time
    '''
    #print('{1:2d}:{}:{}'.format(time.hour,time.minute,time.second))
    print('%.2d:%0.2d:%0.2d' % (time.hour,time.minute,time.second))

def is_after(time1, time2):
    '''
    Return true if time1 is after time2 or false if not

    time1: Time
    time2: Time
    '''
    result = (time1.second + (time1.minute + time1.hour * 60) * 60) > (time2.second + (time2.minute + time2.hour * 60) * 60)
    print(result)

def main():
    time = Time()
    time.hour = 2
    time.minute = 59
    time.second = 3

    time2 = Time()
    time2.hour = 1
    time2.minute = 59
    time2.second = 30
    print_time(time)
    print_time(time2)
    is_after(time, time2)

if __name__ == "__main__":
    main()
