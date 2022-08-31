def calcularIMC(peso, altura):
    imc = peso / (altura * altura)
    return imc;

def clasificarIMC(valorIMC):
    resultadoIMC = round(valorIMC, 1);

    if (valorIMC > 40):
        print(f"\tMi IMC: {resultadoIMC} - Obesidad Grado 3 (muy obeso)");
    elif (valorIMC >= 35 and valorIMC <= 39.9):
        print(f"\tMi IMC: {resultadoIMC} - Obesidad Grado 2 (obeso)");
    elif (valorIMC >= 30 and valorIMC <= 34.9):
        print(f"\tMI IMC: {resultadoIMC} - Obesidad Grado 1 (moderado)");
    elif (valorIMC >= 25 and valorIMC <= 29.9):
        print(f"\tMi IMC: {resultadoIMC} - Sobrepeso (aumentado de peso)");
    elif (valorIMC >= 18.5 and valorIMC <= 24.9):
        print(f"\tMi IMC: {resultadoIMC} - Peso normal");
    else:
        print("\tPeligro, visite a un medico");

    return valorIMC;


if __name__ == "__main__":
    cont = 1;
    
    print("Calcule su IMC");
    print("----------------");
    while (cont != 0):
        nombre = input("NOMBRE: ");
        peso = int(input("PESO: "));
        altura = float(input("ALTURA (Ej: 1.70): "));
        print("== RESULTADO ==");

        indiceMasaCorporal = calcularIMC(peso, altura);
        clasificarIMC(indiceMasaCorporal);

        cont = int(input("\nDesea continuar? 1 - Si / 0 - No: "));
        print("");