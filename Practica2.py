class AnalizadorNumeros:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.numeros = []

    def obtener_lista_numeros(self):
        for i in range(self.cantidad):
            try:
                numero = int(input(f"Ingrese el número {i + 1}: "))
                self.numeros.append(numero)
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
                return self.obtener_lista_numeros()
        return self.numeros

    def analizar_numeros(self):
        numeros_ordenados = sorted(self.numeros)

        print("\nNúmeros ordenados:", numeros_ordenados)

        pares = [num for num in numeros_ordenados if num % 2 == 0]
        impares = [num for num in numeros_ordenados if num % 2 != 0]

        print("\nNúmeros pares:", pares)
        print("Números impares:", impares)

        repetidos = {}
        for num in numeros_ordenados:
            if num in repetidos:
                repetidos[num] += 1
            else:
                repetidos[num] = 1

        print("\nNumero de repeticiones:")
        for num, repeticiones in repetidos.items():
            print(f"{num}: {repeticiones} veces")

def main():
    try:
        cantidad_numeros = int(input("Ingrese la cantidad de números que desea leer: "))
        analizador = AnalizadorNumeros(cantidad_numeros)
        numeros = analizador.obtener_lista_numeros()
        analizador.analizar_numeros()
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
