list_entries = open('day1_input.txt','r')
entries = list(list_entries)
processed = []
for i in range(0, len(entries)):
    item = entries[i].rstrip()
    processed.append(int(item))

print(processed)
seen = dict()
for i in processed:
    seen[2020-int(i)] = True

    if int(i) in seen.keys():
        found = int(i)
        pair = 2020 - found
        print(found)
        print(pair)


multi = found * pair
print(multi)