def dados():
    peso = float(input("Digite seu peso"))
    altura = float(input("Digite sua Altura"))

    imc = peso / (altura ** 2)
    print (f"seu imc é {imc}")
    if imc < 18.5:
        print("abaixo do peso")
    elif imc < 25:
        print ("peso normal")
    elif imc < 30:
        print ("sobrepeso")
    elif imc < 34:
        print ("obesidade I")
    elif imc < 39:
        print ("obesidade II")
    elif imc > 40:
        print("Obesidade III")
dados()