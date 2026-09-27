#for i in range(10): diz quantas vezes o programa vai rodar, nesse caso 10 vezes
for i in range(10):

    nome = input("digite seu nome: ")
    # validando se o nome é vazio ou se é um número, caso seja, ele pede para digitar novamente
    while nome == "" or nome.isnumeric():
        #se for digitado numero vai dar como incorreto
        print("Nome inválido, digite novamente\n")
        nome = input("digite seu nome: ")
     
    #toda vez que o usuário digitar um nome inválido, ele vai pedir para digitar novamente 

    idade = input("digite sua idade: ")
    while not idade.isdigit() or int(idade) < 0:
        #se a idade não for numero ou inteiro o programa exibe a mensagem
        print("numero invalido, digite novamente\n")
        idade = input("digite sua idade: ")
    
    #toda vez que o numero for incorreto ele retorna a pergunta
    
    # Lendo como string primeiro para evitar crash com letras
    avaliação = input("nos diga sua opnião( 1- excelente, 2- mediana, 3- ruim): ")
    while not avaliação.isnumeric() or not (1 <= int(avaliação) <= 3):
        print("Opinião invalida, Digite novamente")
        avaliação = input("nos diga sua opinião( 1- excelente, 2- mediana, 3- ruim):\n ")
    
    # Converte para inteiro só depois que passou da validação
    avaliação = int(avaliação)
#transforma  os numeros das opções em texto.
    opção_de_texto = ["", "excelente", "mediana", "ruim"]
    #é necessario ter aspas vazias antes do excelente se não n escolhe as opções 
    texto_avaliação = opção_de_texto[avaliação]
#saida no looping
    print("Usuario", nome + ".", "você tem", idade, " anos e sua opnião foi", texto_avaliação +".\n")

    print("Obrigado por sua avaliação, sua opnião é muito importante para nós!\n")
# saida quando o looping acaba
print("Obrigado a todos por nos avaliar")
