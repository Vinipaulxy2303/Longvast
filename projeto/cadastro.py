from limpa_tudo import limpatela
from mostrar_cadastro import mostrar_cadastro
from espera import esperar
def cadastro():
    print("====== CADASTRO DE ENTREGA ======  ")
    timer=1
    codigo= []
    entregas= []
    sistema0= False
    while sistema0 == False:
        codigo_texto=input("Qual a sua escolha: (sim / nao) ")
        while not codigo_texto.isalnum():
            print('Escolha inexistente')
            codigo_texto=input("Qual a sua escolha: ")
        sn=str(codigo_texto)
        if sn == "sim":
            codigo_texto = input("Me de um codigo: ")
            while not codigo_texto.isdigit() or int(codigo_texto) <1:
                print("Digite só números!")
                codigo_texto = input("Me de um codigo: ")
            codigos = int(codigo_texto)
            sistema = True
            if timer > 1:
                while sistema == True:
                    if codigos in codigo:
                        print("Repetido!")
                        codigos=int(input("Me de um codigo: "))
                    else:
                        sistema = False
                        codigo.append(codigos) 
            else:
                codigo.append(codigos)      
            nome_ou_descrição_do_destinatário=str(input("Qual o nome : "))
            codigo_texto =input("""Qual a região de origem: 
            1. Centro
            2. Norte
            3. Sul
            4. Leste
            5. Oeste
            """)
            while not codigo_texto.isdigit() or int(codigo_texto) < 1 or int(codigo_texto) > 5:
                print('Opção Invalida')
                codigo_texto=input("Qual a região de origem: ")
            região_de_origem= int(codigo_texto)
            codigo_texto =input("""Qual é o destino final: 
            1. Centro
            2. Norte
            3. Sul
            4. Leste
            5. Oeste
            """)
            while not codigo_texto.isdigit() or int(codigo_texto) < 1 or int(codigo_texto) > 5:
                print('Opção Invalida!')
                codigo_texto=input("Qual é o destino final: ")
            destino_final=int(codigo_texto)
            peso_da_carga =float(input("QUal é o peso da carga: "))
            valor_da_mercadoria =float(input("Qual é o valor de mercado: "))
            print("""1 - Urgente
2 - Prioritária
3 - Normal
    """)
            codigo_texto = input("Qual a sua prioridade: ")
            while  not codigo_texto.isdigit() or int(codigo_texto) < 1 or int(codigo_texto) > 3:
                print("Prioridade Invalida!")
                codigo_texto=input("Qual a sua prioridade: ")
            prioridade= int(codigo_texto)
            print("""1 - Aguardando
2 - Em transporte
3 - Entregue
""")
            codigo_texto= input("Qual é status atual? ")
            while not codigo_texto.isdigit() or int(codigo_texto) <1 or int(codigo_texto) > 3:
                print("Status Invalido!")
                codigo_texto= input("Qual é o status atual? ")
            status= int(codigo_texto)
            print('Status registrado!!')
            custo_estimado_da_entrega =float(input("Qual é o valor estimado para a entrega: "))
            codigo_texto = input("Qual a distância total: ")
            while not codigo_texto.isdigit():
                    print("Digite só números!")
                    codigo_texto = input("Qual a distância total: ")
            distancia=int(codigo_texto)
            limpatela()
            timer += 1
            entrega={"Codigo": codigos ,
                     "nome ou descrição do destinatário" : nome_ou_descrição_do_destinatário ,
                     "região de origem": região_de_origem,
                     "região de destinada": destino_final,
                     "peso da carga": peso_da_carga,
                     "valor da mercadoria": valor_da_mercadoria,
                     "prioridade":prioridade,
                     "distância": distancia,
                     "status": status,
                     "custo estimado da entrega":custo_estimado_da_entrega
                     }
            entregas.append(entrega) 
        elif sn == 'nao':
            sistema0 = True
            mostrar_cadastro(entregas)
            opcao=input("Só apertar enter")
            limpatela()
            esperar()
    return entregas
