def e2(cadena, new=""):
    if len(cadena) != 0:
        tamano = len(cadena)
        new += cadena[tamano-1]
        return e2(cadena[:tamano-1], new)
    else:
        return new


x = "Juan Camilo David"
print(e2(x))
