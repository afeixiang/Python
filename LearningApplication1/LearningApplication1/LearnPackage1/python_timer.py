'''
Create a timer that rings every 30 minutes
'''
import threading

def timer_print():
    '''
    main timer function
    '''
    print('---begin--')
    threading.Timer(5.0, hello).start()
    #print('It is up!')
    print('---end--')

def hello():
    '''
    print something to show that the timer is end
    '''
    print("hello, Timer")

if __name__ == '__main__':
    timer_print()
