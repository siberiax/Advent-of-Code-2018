import sys
from collections import defaultdict

words = []

for line in open(sys.argv[1]):
    words.append(line.strip())

twos = 0
threes = 0
diff_found = 0

for word1 in words:
    l = len(word1)
    num_chars = defaultdict(int)
    for char in word1:
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    twos_set = 1
    threes_set = 1
    for char,num in num_chars.items():
        if twos_set and num == 2:
            twos += 1
            twos_set = 0
        if threes_set and num == 3:
            threes += 1
            threes_set = 0
    if not diff_found:
        for word2 in words:
            if word1 != word2:
                different = 0
                diff_char = ""
                for i in range(l):
                    if word1[i] != word2[i]:
                        different += 1
                        diff_char = word1[i]
                if different == 1:
                    print(word1.replace(diff_char, ""))
                    diff_found = 1
                    break

print(twos * threes)
