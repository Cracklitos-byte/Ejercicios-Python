def area_circulo(radio=5):
    # area = PI * radio ** 2
    return 3.1416 * (radio ** 2)


def main():
    radio = int(input("Introduce el radio del circulo\n"))
    print(area_circulo(radio))


if __name__ == "__main__":
    main()
