# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    output_str = ' '.join(map(str, output))
    #print(' '.join(map(str, output)))
    print(output_str)
    
def rabin_karp(pattern, text):
    prime = 101
    p_hash = 0
    for i in range(len(pattern)):
        p_hash += ord(pattern[i]) * pow(prime, i)
    p_hash %= prime

    t_hash = 0
    positions = []
    for i in range(len(text) - len(pattern) + 1):
        if i == 0:
            for j in range(len(pattern)):
                t_hash += ord(text[j]) * pow(prime, j)
        else:
            t_hash = (t_hash - ord(text[i-1])) / prime
            t_hash += ord(text[i+len(pattern)-1]) * pow(prime, len(pattern)-1)
        
        if t_hash == p_hash:
            if text[i:i+len(pattern)] == pattern:
                positions.append(i)

    return positions

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    # and return an iterable variable
    return rabin_karp(pattern, text)


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

