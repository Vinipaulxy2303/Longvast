from limpa_tudo import limpatela
def mostrar_cadastro(entregas):
    sistema0= False
    print("""
========== LISTAR ENTREGAS ==========""")
    while sistema0 == False:
        codigo_texto=input("Qual a sua escolha: (sim / nao) ")
        while not codigo_texto.isalnum():
                print('Escolha inexistente')
                codigo_texto=input("Qual a sua escolha: ")
        sn=str(codigo_texto)
        if sn == 'sim':
            while True:
                    try:
                        texto=input('Qual codigo você quer procurar: ')
                        procura=int(texto)

                        entrega_encontrada = next(
                            (entrega for entrega in entregas if entrega["Codigo"] == procura),
                            None,
                        )
                        if entrega_encontrada is None:
                            raise ValueError("Código não encontrado")

                        for chave, valor in entrega_encontrada.items():
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
                        input("Só apertar enter")
                        limpatela()
                            
                    except ValueError:
                        print("tente novamente")
                        input("Só apertar enter")
                        limpatela()
        elif sn == 'nao':
             sistema0 = True 
             limpatela() 