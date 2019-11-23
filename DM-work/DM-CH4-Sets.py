conjunto = set()

conjunto1 = {1, 3, "a"}

print(conjunto)
print(conjunto1)

print(3 in conjunto1)

conjunto.add("a")
print(conjunto)
conjunto1.discard(1)
print(conjunto1)

conjunto.update(conjunto1)

print(conjunto)
print(dir(conjunto1))
