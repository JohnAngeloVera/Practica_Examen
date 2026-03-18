def calculadora_simple (numero1:int, numero2:int ) -> None:

    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2 if numero2 != 0 else 0
    print(f"{suma}\n{resta}\n{multiplicacion}\n{division}")


if __name__ == "__main__":
    calculadora_simple(4,3)
    calculadora_simple(80,20)
    calculadora_simple(2,0)