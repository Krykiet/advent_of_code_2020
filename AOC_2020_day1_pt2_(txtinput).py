list_entries = open('day1_input.txt','r')
entries = list(list_entries)
processed = []
for i in range(0, len(entries)):
    item = entries[i].rstrip()
    processed.append(int(item))
breaker = False
print(processed)
seen = dict()
sums = set()
for n in processed:
    seen[2020-int(n)] = True
for i in range(0, len(seen)):
    for j in range(1, len(seen)):
        sum_entries = processed[j]+processed[i]
        if sum_entries in seen.keys():
            found1 = processed[i]
            found2 = processed[j]
            pair = 2020 - found1 - found2
            print('gotcha')
            print(found1, found2)
            print(pair)
            breaker = True
            break
    if breaker:
        break

multi = found1 * found2 * pair
print(multi)