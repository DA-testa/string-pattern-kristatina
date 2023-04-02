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
    output_str = ' '.join(map(str, output)).replace('\n',' ')
    #print(' '.join(map(str, output)))
    print(output_str)

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    # and return an iterable variable
    p = len(pattern)
    t = len(text)

    pattern_hash = sum(ord(pattern[i]) * pow(10, p-i-1) for i in range(p))
    text_hash = sum(ord(text[i]) * pow(10, p-i-1) for i in range(p))
    result = []

    for i in range(t-p+1):
        # Check the hash values of current window of text and pattern
        if text_hash == pattern_hash:
            # Check for characters one by one
            match = True
            for j in range(p):
                if text[i+j] != pattern[j]:
                    match = False
                    break
            if match:
                result.append(i)

        if i < t-p:
            text_hash = (text_hash - ord(text[i]) * pow(10, p-1)) * 10 + ord(text[i+p])

    return result

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

