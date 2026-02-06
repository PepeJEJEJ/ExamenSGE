try:
    numero1 = int(input("Dame un numero: "))
    numero2 = int(input("Dame otro numero: "))
    division = int(numero1 / numero2)
    print(division)
except ArithmeticError as error:
    print("Se ha producido el siguiente error aritmético:", str(error))
except Exception as error:
    print("Se ha producido el siguiente error:", str(error))
else:
    print("TA BIEN")
finally:
    print("_______________")