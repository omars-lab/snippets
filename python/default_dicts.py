from collections import defaultdict

string = "The lazy fox jumped over the brown doge."
counter = defaultdict(lambda: 0)
for letter in string:
    counter[letter] += 1

print counter
