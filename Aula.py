#metodo de busca de leitura
with open("Exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print (conteudo)


#abrir um arquivo para escrita
with open("Exemplo2.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("ola mundo")
    arquivo.write("\nhello world")
