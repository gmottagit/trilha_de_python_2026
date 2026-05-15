viavel = True
valor_total = 0
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
        duracao = int(input())

        custo_hospedagem = custo_hospedagem * 6.10  
        custo_hospedagem = custo_hospedagem * duracao
        valor_total = custo_hospedagem + custo_passagem
                
        print(f"O valor total da hospedagem é {custo_hospedagem} reais")
        print(f"O valor total da viagem é {valor_total} reais")

        if orcamento >= valor_total and duracao > 0:
                print("A viagem tem o orçamento possível")
                print(f"Sobram {orcamento - valor_total} reais")
        else:
                print("A viagem não tem orçamento possível")
                print(f"Faltam {valor_total - orcamento} reais")


except ValueError :
        print("Você enviou os dados errados")
        print("Deleting system32...💀")


