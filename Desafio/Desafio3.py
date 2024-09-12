Nome = input("Digite seu nome: ")
Sobrenome = Nome.split()

if len(Sobrenome) > 1:
    print("O sobrenome digitado é: ", Sobrenome[-1])
else:
    print("Não foi digitado nome com sobrenome")