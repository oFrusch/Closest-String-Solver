from collections import Counter

def get_strings(document):
    with open(document,"r") as file:
        lines = [line.replace("\n", "") for line in file]
        lines.pop(0)
    return lines

def hamming_distance(string1, string2):
    dist = 0
    for char1, char2 in zip(string1, string2): 
        if char1 != char2: dist += 1
    return dist

def compute_distances(document):
    strings = get_strings(document)
    counter = Counter(strings)
    for string in strings:
        counter[string] = sum(hamming_distance(string,string2) for string2 in strings)
    min_string = counter.most_common()[-1]
    return min_string


print(compute_distances("strings.txt"))
print(compute_distances("strings2"))