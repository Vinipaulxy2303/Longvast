from matriz_distancia import destino_total
from limpa_tudo import limpatela
from mostrar_cadastro import mostrar_cadastro
from espera import esperar
def cadastro(entregas, codigo):
    print("====== CADASTRO DE ENTREGA ======  ")
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
            while sistema == True:
                if codigos in codigo:
                    print("Repetido!")
                    codigos=int(input("Me de um codigo: "))
                else:
                    sistema = False
                    codigo.append(codigos) 
            nome_ou_descrição_do_destinatário=str(input("Qual o nome : "))
            codigo_texto =input("""1. Centro
2. Norte
3. Sul
4. Leste
5. Oeste
Qual a região de origem: """)
            while not codigo_texto.isdigit() or int(codigo_texto) < 1 or int(codigo_texto) > 5:
                print('Opção Invalida')
                codigo_texto=input("Qual a região de origem: ")
            região_de_origem= int(codigo_texto)
            região_de_origem -= 1
            codigo_texto =input("""1. Centro
2. Norte
3. Sul
4. Leste
5. Oeste
Qual é o destino final: """)
            while not codigo_texto.isdigit() or int(codigo_texto) < 1 or int(codigo_texto) > 5:
                print('Opção Invalida!')
                codigo_texto=input("Qual é o destino final: ")
            destino_final=int(codigo_texto)
            destino_final -= 1
            codigo_texto=float(input("QUal é o peso da carga (Kg): "))
            while not codigo_texto.isdigit() or float(codigo_texto) < 1:
                            print('Opção Invalida!')
                            codigo_texto=input("Qual é o destino final: ")
            peso_da_carga=float(codigo_texto) 
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
            distancia = destino_total(região_de_origem,destino_final)
            if peso_da_carga <= 5:
                custo_estimado_da_entrega=0
                Custo_base = distancia + custo_estimado_da_entrega   # Tem que terminar isso!!!
            elif peso_da_carga > 5 and peso_da_carga <= 20:
                    custo_estimado_da_entrega= 10/100
                    Custo_base= distancia +(valor_da_mercadoria* custo_estimado_da_entrega)
            elif peso_da_carga > 20 and peso_da_carga <= 50:
                 custo_estimado_da_entrega= 20/100
                 Custo_base= distancia + (valor_da_mercadoria* custo_estimado_da_entrega)
            elif peso_da_carga > 50:
                 custo_estimado_da_entrega=35/100
                 Custo_base= distancia + (valor_da_mercadoria* custo_estimado_da_entrega)

            if prioridade == 3:
                 Custo_base + (Custo_base*0)
            elif prioridade == 2:
                Custo_base + (Custo_base*15/100)
            elif prioridade == 1:       #tem que terminar isso 
                 Custo_base + (Custo_base*30/100)
            limpatela() 
            entrega={"Codigo": codigos ,
                     "nome ou descrição do destinatário" : nome_ou_descrição_do_destinatário ,
                     "região de origem": região_de_origem + 1,
                     "região de destinada": destino_final + 1,
                     "peso da carga": peso_da_carga,
                     "valor da mercadoria": valor_da_mercadoria,
                     "prioridade":prioridade,
                     "distância": distancia,
                     "status": status,
                     "custo estimado da entrega":Custo_base
                     }
            entregas.append(entrega) 
        elif sn == 'nao':
            sistema0 = True            
    return entregas,codigo