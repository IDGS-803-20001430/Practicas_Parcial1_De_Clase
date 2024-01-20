class Piramide:
    def __init__(self, altura):
        self.altura = altura

    def imprimir_piramide(self):
        for i in range(1, self.altura + 1):
            espacios = " " * (self.altura - i)
            asteriscos = "* " * i
            print(espacios + asteriscos)

def main():
    try:
        altura_piramide = int(input("Ingrese un número para la altura de la pirámide: "))
        piramide = Piramide(altura_piramide)
        piramide.imprimir_piramide()
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
