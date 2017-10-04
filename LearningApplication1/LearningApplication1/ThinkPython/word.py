def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def is_palindrome(string):
    '''
    Returen whether the input string is palindrome

    string:string
    '''
    if len(string) == 1 or len(string) == 0:
        return True
    if first(string) == last(string):
        return is_palindrome(middle(string))
    else:
        return False


for i in range(3):
    print('Hello!')
#print(is_palindrome('ter'))