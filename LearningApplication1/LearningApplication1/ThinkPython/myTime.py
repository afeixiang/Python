'''
For practice time function.
'''
import time

def m_minutes(s):
    '''
    Calculate minutes from seconds

    s:seconds
    '''
    m = s//60
    return m

def m_hours(m):
    '''
    Calculate hours from minutes

    m:minutes
    '''
    h = m//60
    return h

def m_days(h):
    '''
    Calculate days from hours

    h:hours
    '''
    d = h//24
    return d
print(m_minutes(time.time()))
print(m_hours(m_minutes(time.time())))
print(m_days(m_hours(m_minutes(time.time()))))
