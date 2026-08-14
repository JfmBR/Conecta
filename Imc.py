peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura"))

imc = peso / (altura ** 2)

if imc < 18.5:
    print (f"Seu IMC deu {imc}\n"
           "abaixo do peso")
elif imc >= 18.5 and imc < 24.9:
    print (f"Seu IMC deu {imc}\n"
               "Você está normal")
elif imc >= 25:
    print (f"Seu IMC deu {imc}\n"
               "Você está soprepeso")
