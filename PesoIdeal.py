# IMC - peso Ideal
# Peso ideal é igual ao Peso dividido pela Altura ao quadrado

N = input("Digite o seu nome: ")
c = float(input("qual sua altura em m: "))
b = float(input("qual seu peso em kg: "))
s = input("qual seu genero H (HOMEM), M (MULHER): ")
IMC = b / (c ** 2)


if IMC < 16.0:
    print(
        N, "Voce esta com baixo peso, muito grave - {:.2f}" .format(b), ("kg"))
    p = ((c ** 2) * 21.75)
    print("Seu peso ideal é = {:.2f} " .format(p), ("kg"))
    i = (b - p)
    print(N, "voce esta {:.2f}" .format(i), ("kg abaixo do peso ideal."))


elif IMC > 16.0 and IMC <= 16.99:
    print(N, "Voce esta com baixo peso, grave - {:.2f}" .format(b), ("kg"))
    p = ((c ** 2) * 21.75)
    print("Seu peso ideal é = {:.2f} " .format(p), ("kg"))
    i = (b - p)
    print(N, "voce esta {:.2f}" .format(i), ("kg abaixo do peso ideal."))

elif IMC > 17.0 and IMC <= 18.49:
    print(N, "Voce esta com abaixo do peso - {:.2f}" .format(b), ("kg"))
    p = ((c ** 2) * 21.75)
    print("Seu peso ideal é = {:.2f} " .format(p), ("kg"))
    i = (b - p)
    print(N, "voce esta {:.2f}" .format(i), ("kg abaixo do peso ideal."))

elif IMC > 18.50 and IMC <= 24.99:
    print("Voce esta com peso ideal - {:.2f}" .format(b), ("kg"))
    print("Parabéns! Continue assim.")


elif IMC > 25.0 and IMC <= 29.99:
    print(N, "voce está com sobrepeso!")
    print("Seu IMC é: {:.2f}" .format(IMC))
    p = ((c ** 2) * 21.75)
    print("Seu peso ideal é = {:.2f} " .format(p), ("kg"))
    i = (b - p)
    print(N, "voce esta {:.2f}" .format(i), ("kg acima do peso ideal."))
    print("------------------------------------")
    print("10 dicas para perder e manter o peso")
    print("Coma alimentos saudáveis, em porções saudáveis. ...")
    print("Faça mais atividades físicas. ...")
    print("Coma mais frutas e vegetais. ...")
    print("Simplifique a medição das porções. ...")
    print("Anote tudo. ...")
    print("Livre-se de cinco hábitos ruins e adote cinco hábitos bons. ...")
    print("Conheça a medida de sua cintura....")
    print("Não se sacrifique em demasia.")


elif IMC > 30.0 and IMC <= 34.99:
    print(N, "voce esta com obesidade Grau 1 - {:.2f} " .format(b), ("kg"))
    p = ((c ** 2) * 21.75)
    print("Seu peso ideal é = {:.2f} " .format(p), ("kg"))
    i = (b - p)
    print(N, "voce esta {:.2f}" .format(i), ("kg acima do peso ideal."))

elif IMC > 35.0 and IMC <= 39.99:
    print(N, "Voce esta com obesidade grau 2 - {:.2f} " .format(b), ("kg"))
    p = ((c ** 2) * 21.75)
    print("Seu peso ideal é = {:.2f} " .format(p), ("kg"))
    i = (b - p)
    print(N, "voce esta {:.2f}" .format(i), ("kg acima do peso ideal."))

elif IMC > 40.0 and IMC < 50:
    print(N, "Voce esta com obesidade grau 3, - {:.2f} " .format(b), ("kg"))
    p = ((c ** 2) * 21.75)
    print("Seu peso ideal é = {:.2f} " .format(p), ("kg"))
    i = (b - p)
    print(N, "voce esta {:.2f}" .format(i), ("kg acima do peso ideal."))
else:
    print(N, "PROCURE UM MEDICO URGENTE !!! - {:.2f}" .format(b), ("kg"))
    p = ((c ** 2) * 21.75)
    print("Seu peso ideal é = {:.2f} " .format(p), ("kg"))
    i = (b - p)
    print(N, "voce esta {:.2f}" .format(i), ("kg acima do peso ideal."))
