lista = ["futbol",123,"tenis","hola",45,"python"]

palabras = []

for elemento in lista:
    if type(elemento) == str:
        palabras.append(elemento)

mayor = max(palabras)

print("palabras encontrados:", palabras)
print(len(palabras))