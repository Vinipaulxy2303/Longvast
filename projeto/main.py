from tela_inicial import tela_inicial
continuar = True
entregas = []
while continuar == True:
    escolha, entregas = tela_inicial(entregas)
    if escolha ==  10:
        continuar = False
    else:
        continuar= True