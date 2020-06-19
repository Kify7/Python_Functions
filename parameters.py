def greet(lang) :
    if lang == "es" :
        print("hola")
    elif lang == "fr" :
        print("Bonjour")
    else:
        print("Hello")

greet("es")
greet("fr")
greet("en")

def salut() :
    return "Hello"

print(salut(), "Glenn")
print(salut(), "Kify")