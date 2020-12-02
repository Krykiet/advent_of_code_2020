import sys
print('After pasting the multiline input in console press ctrl+D')
list_entries = sys.stdin.read() # after giving the input press ctrl+d
entries = list_entries.splitlines()
seen = dict()
for i in entries:
    seen[2020-int(i)] = True
    if int(i) in seen.keys():
        found = int(i)
        pair = 2020 - found
        print(found)
        print(pair)

multi = found * pair
print(multi)