def print_upper_words(words):
    """Prints each word on a seperate line and turn it into uppercase"""


    for word in words:
        print(word.upper()) 

def print_upper_words_two(words):
    """Prints words on a seperate line, uppercased, if it starts with E or e"""


    for word in words:
        if word.startswith('e') or word.startswith("E"):
            print(word.upper())

def print_upper_words_three(words, starts_with):
    """Prints each word on a seperate line, uppercase, if it starts with letter given"""

    
    for word in words:
        for char in starts_with:
            if word.startswith(char):
                print(word.upper())
