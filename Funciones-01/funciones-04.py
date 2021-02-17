def intermedio(a, b):
    # Numero intermedio = suma de los numeros entre 2
    return (a + b) / 2


def main():
    numero_a = int(input("Introduce el primer numero:\n"))
    numero_b = int(input("Introduce el segundo numero:\n"))
    print(
        f"El punto intermedio de {numero_a} -- {numero_b} es: {intermedio(numero_a, numero_b)}")


if __name__ == "__main__":
    main()
