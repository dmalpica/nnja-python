def mifuncion(arg1, arg2):
    return arg1 + arg2


def hello_world(arg1, arg2):
    return (f"{arg1}, {arg2}.")

# hello_world("Hello", "World")


hello = hello_world("Hello", "World")

print(hello)


def say_greeting(greeting, name):
    greet = (f"{greeting}, {name}.")
    return greet


sg = say_greeting("hola", "david")
print(sg)


def greeting_with_default(greeting, name="David", mark="!"):
    return (f"{greeting}, {name}{mark}")


print(greeting_with_default("Hey", "Sarah", "?"))
print(greeting_with_default("Hola"))
print(greeting_with_default("Ole"))


def create_query(language="C#", num_stars=50, sort="desc"):
    return f"Lengua:{language} Estrellas:{num_stars} orden:{sort}"


print(create_query())

print(greeting_with_default("Hey", mark="?", name="Sarah"))

# functions practice


def operate_numbers(x, y, operation="add"):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y


print(f"The suma of 1 and 2 is {operate_numbers(1, 2)}")
print(f"The resta of 1 and 2 is {operate_numbers(1, 2, 'subtract')}")
