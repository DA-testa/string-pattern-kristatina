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
    pattern = input().strip()
    text = input().strip()
    return pattern, text

def print_occurrences(positions):
    print(" ".join(map(str, positions)))


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

