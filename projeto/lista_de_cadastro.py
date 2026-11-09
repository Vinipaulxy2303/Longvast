
def lista(entregas):
    for chave, valor in entregas.items():
        if chave == "peso da carga":
            valor_formatado = f"{valor:.2f}".replace(".", ",")
            print(f"{chave}: {valor_formatado} Kg")
        elif chave == "valor da mercadoria":
            valor_formatado = f"{valor:.2f}".replace(".", ",")
            print(f"{chave}: R$ {valor_formatado}")
        elif chave == "distância":
            print(f"{chave}: {valor} Km")
        elif chave == "custo estimado da entrega":
            valor_formatado = f"{valor:.2f}".replace(".", ",")
            print(f"{chave}: R$ {valor_formatado}")
        else:
            print(f"{chave}: {valor}")
        print("-" * 30)