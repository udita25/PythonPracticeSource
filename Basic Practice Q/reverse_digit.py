from collections import Counter

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
c = Counter(a)
f = c.most_common(3)[2][0]  # Get the element with highest frequency

print(f)