programa = True
while programa == True:
    try:
        print("Digite o orçamento (Use . para casas decimais): ")
        orcamento = float(input())
        print("Digite o destino (cidade/país): ")
        destino = str(input())
        print("Digite o custo da passagem (Em reais): ")
        custo_passagem = float(input())
        print("Digite o custo da hospedagem (em Euros): ")
        custo_hospedagem = float(input())
        print("Digite a duração da viagem (em dias): ")
        custo_hospedagem = int(input())

    
    except ValueError :
        print("Você enviou os dados errados")
        print("Deleting system32...💀")
        programa = False


