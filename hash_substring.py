"""
Sintija Norkārkle, RDCPO, 1. grupa
"""

# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow

    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    source = input()
    
    if "I" in source:
        pattern = input()
        text = input()
    elif "F" in source:
        with open("./tests/06", mode = "r") as fails:
            pattern = fails.readline()
            text = fails.readline()
    # ja lietotājs norādīja nederīgu ievades avotu, tiek izdrukāts kļūdas paziņojums
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
    
    # ja meklējamās rakstzīmju virknes garums ir lielāks par teksta garumu, tad atgriežam tukšu sarakstu
    if len(pattern) > len(text):
        return []
    
    # definēti mainīgie, kuri tiks izmantoti vēlāk
    hashmod = 10**9 + 7
    multiplier = 31
    text_length = len(text)
    pattern_length = len(pattern)
    rm = pow(multiplier, pattern_length - 1, hashmod)
    p_hash = t_hash = 0

    # tiek aprēķinātas hash vērtības gan meklējamai rakstzīmju virknei, gan pirmajai tekstā sastopamajai virknei
    for i in range (pattern_length) :
        p_hash = (pow(multiplier, 1, hashmod) * p_hash + ord(pattern[i])) % hashmod
        t_hash = (pow(multiplier, 1, hashmod) * t_hash + ord(text[i])) % hashmod

    # tiek izveidots tukšs saraksts, kurā tiks saglabātas meklējamo rakstzīmju virkņu atrašanās vietas tekstā
    list = []

    # tiek salīdzinātas hash vērtības, lai atrastu visus vienādos fragmentus, kurus pēc tam pievieno sarakstam
    for i in range (text_length - pattern_length + 1):
        if hash(pattern) == hash(text[i : i + pattern_length]):
            list.append(i)

    # ja visa virkne nav pārbaudīta, tad turpina to darīt un pārbauda, vai ir vēl kāda vieta, kur ir vienādi fragmenti
    if i < text_length - pattern_length:
        t_hash = ((multiplier * t_hash) % hashmod - (multiplier * ord(text[i] * rm) % hashmod + ord(text[i + pattern_length]))) % hashmod

    # ja hash vērtība ir negatīva, tad tai jāpieskaita hashmod, lai iegūtu pozitīvu vērtību
        if t_hash < 0 :
            t_hash += hashmod
    
    # and return an iterable variable
    return list


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
