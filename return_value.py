def saludo(lang) :
    if lang == "es" :
        return "hola"
    elif lang == "fr" :
        return "bonjour"
    else :
        return "hi!"

print(saludo("es"))
print(saludo("fr"))
print(saludo(" "))


def addtwoo(a, b) :
    added = a + b
    return added

print(addtwoo(6, 5))
