names = ["Nina",
         "Max",
         "Jane",
         ]
print(len(names))
print(names[0])
print(names[1])
print(names[2])

names[2] = "Floyd"

print(names[2])

help(list.append)
names.append("David")
print(names[3])

noms = sorted(names)
print(noms)

nomsreverse = sorted(names, reverse=True)
print(nomsreverse)

names.sort()
print(names)
names.sort(reverse=True)
print(names)
names.reverse()
print(names)

names.insert(2, "Sarah")
print(names)

names.extend(noms)

print(names)
