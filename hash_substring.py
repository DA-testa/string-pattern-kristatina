# python3

def rabin_karp(pattern, text):
    p_len = len(pattern)
    t_len = len(text)
    p_hash = hash(pattern)
    t_hash = hash(text[:p_len])
    positions = []
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            if text[i:i+p_len] == pattern:
                positions.append(i)
        if i < t_len - p_len:
            t_hash = hash(text[i+1:i+p_len+1])
    return positions


def get_occurrences(pattern, text):
    return rabin_karp(pattern, text)


def read_input():
    str = input()

    if "I" in str:
        p = input()
        t = input()   
    elif "F" in str:
        fileName = "./tests/06"
        file = open(fileName, "r")
        p = file.readline()
        t = file.readline()

    return (p.rstrip(), t.rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

