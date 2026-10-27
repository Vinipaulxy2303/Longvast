from tela_inicial import tela_inicial
continuar = True
entregas =[]
codigo= []
while continuar == True:
    escolha, entregas ,região_de_origem, codigo = tela_inicial(entregas,região_de_origem, codigo)
    if escolha ==  10:
        continuar = False
    else:
        continuar= True