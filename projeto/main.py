from tela_inicial import tela_inicial
continuar = True
entregas =[]
codigo= []
while continuar == True:
    escolha, entregas, codigo = tela_inicial(entregas, codigo)
    if escolha ==  10:
        continuar = False
    else:
        continuar= True