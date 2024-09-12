lista = ["maca", "banana", "laranja"]
print("lista de frutas:", lista)

adicionarfruta = input("Adicione uma fruta: ")


lista.append(adicionarfruta)
 
print(lista)


removerfruta = input("Remova uma fruta: ")

if removerfruta in lista:
    lista.remove(removerfruta)
    print("Item removido, lista atualizada: ",lista)
else:
    print("Item inexistente na lista, tente novamente")
