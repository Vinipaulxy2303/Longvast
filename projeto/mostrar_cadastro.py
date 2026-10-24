from espera import esperar
def mostrar_cadastro(entregas):
    for entrega in entregas :
        for chave, valor in entrega.items():
            if chave == "peso da carga":
                print(f"{chave}:{valor} Kg")
            elif chave == "valor da mercadoria":
                print(f"{chave}:R${valor}")
            elif chave == "distância":
                print(f"{chave}:{valor} Km")
            elif chave == "custo estimado da entrega":
                print(f"{chave}:R${valor}")
            else:
               print(f"{chave}: {valor}")
        print("-" * 30)
        opcao=input("Só apertar enter")
        esperar()