import cadastro 
def mostrar_cadastro(entergas):
    for entrega in entergas :
        for chave, valor in entrega.items():
            print(f"{chave}: {valor}")
        print("-" * 30)