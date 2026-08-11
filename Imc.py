peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura"))

imc = peso / (altura * altura)

if imc < 18.5:
    print (f"Seu IMC deu {imc}\n"
           "Você está magro")
elif imc > 24.9:
    print (f"Seu IMC deu {imc}\n"
               "Você está normal")
elif imc >29.9:
    print (f"Seu IMC deu {imc}\n"
               "Você está soprepeso")
elif imc >39.9:
    print (f"Seu IMC deu {imc}\n"
               "Você está obeso")