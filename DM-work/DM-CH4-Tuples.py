# tuples are immutable
tup = ()
print(type(tup))

tup1 = (1, )  # trailing comma is necesary for correct tuple class
tup2 = (1, "a", 3)
print(tup1)
print(tup2)

print("index:", tup2.index("a"))

student = ("Marcy", 8, "History", 3.5)

print("student", student[0])

# student[0] = "Bob" #error: tuple is inmutable

nom, edad, sujeto, grado = student  # unpacking

print("nombre", nom)


def http_status_code():
    return 200, "OK"


code, value = http_status_code()

print("codigo:", code)
