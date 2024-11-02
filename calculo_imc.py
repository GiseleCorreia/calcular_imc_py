def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Desnutrição"
    elif 18.5 <= imc < 24.9:
        return "Peso Ideal"
    elif 25 <= imc < 29.9:
        return "Acima do Peso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

def main():
    print("Calculadora de IMC")
    try:
        peso = float(input("Informe seu peso em kg: "))
        altura = float(input("Informe sua altura em metros: "))
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        print(f"Seu IMC é: {imc:.2f} - {classificacao}")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()

