def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


def main():
    numero_a = int(input("Introduce el primer numero\n"))
    numero_b = int(input("Introduce el segundo numero\n"))
    print(relacion(numero_a, numero_b))


if __name__ == "__main__":
    main()
