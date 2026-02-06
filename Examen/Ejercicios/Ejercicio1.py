def ConvertirBin(precio):
    precio_final = ''

    if precio:
        precio_final = str(precio + 21)
        precio = precio * 0.21
    return str(precio) + precio_final

fich = open("precio.txt", "r")
dec = fich.read()
fich.close()

precio_final = ConvertirBin(int(dec))

fich = open("precio_final.txt", "w")
fich.write(precio_final)
fich.close()