def calcular_capital_final(capital_inicial, interes, anys):
    """Calcula el capital final després d'un cert nombre d'anys amb un interès compost."""
    return capital_inicial * (1 + interes / 100) ** anys

def main():
    print("Benvingut al calculador de capital final!")

    # Demanar capital inicial
    while True:
        capital = float(input("Introdueix la quantitat a sol·licitar (50000€ - 800000€): "))
        if 50000 <= capital <= 800000:
            break
        else:
            print("Error: La quantitat ha de ser entre 50000€ i 800000€.")

    # Demanar interès
    while True:
        interes = float(input("Introdueix l'interès (0.5% - 13%): "))
        if 0.5 <= interes <= 13:
            break
        else:
            print("Error: L'interès ha de ser entre 0.5% i 13%.")

    # Demanar anys
    while True:
        anys = int(input("Introdueix el número d'anys (3 - 40): "))
        if 3 <= anys <= 40:
            break
        else:
            print("Error: El número d'anys ha de ser entre 3 i 40.")

    # Calcular el capital final
    capital_final = calcular_capital_final(capital, interes, anys)

    # Mostrar el resultat
    print(f"El capital final després de {anys} anys és: {capital_final:.2f}€")

# Executar el programa
if __name__ == "__main__":
    main()