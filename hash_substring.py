# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow

    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    source = input("Enter the input source: ")
    if "I" in source:
        pattern = input()
        text = input()
    elif "F" in source:
        with open("./tests/06", mode = "r") as fails:
            pattern = fails.readline()
            text = fails.readline()
    else :
        print("Invalid input source")

    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern.rstrip(), text.rstrip())


def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    
    if len(pattern) > len(text):
        return []
    
    hashmod = 10**9 + 7
    multiplier = 31
    text_length = len(text)
    pattern_length = len(pattern)

    rm = pow(multiplier, pattern_length - 1, hashmod)
    p_hash = t_hash = 0

    for i in range (pattern_length) :
        p_hash = (pow(multiplier, 1, hashmod) * p_hash + ord(pattern[i])) % hashmod
        t_hash = (pow(multiplier, 1, hashmod) * t_hash + ord(text[i])) % hashmod

    occurrences = []

    for i in range (text_length - pattern_length + 1):
        if hash(pattern) == hash(text[i : i + pattern_length]):
            occurrences.append(i)

    if i < text_length - pattern_length:
        t_hash = ((multiplier * t_hash) % hashmod - (multiplier * ord(text[i] * rm) % hashmod + ord(text[i + pattern_length]))) % hashmod

        if t_hash < 0 :
            t_hash += hashmod
    
    # and return an iterable variable
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

