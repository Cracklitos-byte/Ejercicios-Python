def area_rectangulo(base = 15, altura = 10):
    return base * altura

def main():
    base = int(input("Introduzca la base del rectangulo\n"))
    altura = int(input("Introduzca la altural del rectangulo\n"))
    print(area_rectangulo(base,altura))

if __name__ == "__main__":
    main()
