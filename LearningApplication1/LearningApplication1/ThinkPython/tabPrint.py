'''
Print a table with four rows and four columns
'''
def print_row_line():
    '''
    print the row line
    '''
    print('+', end=' ')
    print('- - - +', end=' ')
    print('- - - +', end=' ')
    print('- - - +', end=' ')
    print('- - - +')

def print_column_line():
    '''
    print the four columns' line
    '''
    print_one_column_line()
    print_one_column_line()
    print_one_column_line()
    print_one_column_line()

def print_one_column_line():
    '''
    print the one columns' line
    '''
    print('|       |', end=' ')
    print('      |', end=' ')
    print('      |', end=' ')
    print('      |')

def print_one_row():
    '''
    print a one row table with four columns
    '''
    print_row_line()
    print_column_line()

def print_table():
    '''
    print the table with four rows and four columns.
    '''
    print_one_row()
    print_one_row()
    print_one_row()
    print_one_row()
    print_row_line()

print_table()
