from matriz_distancia import destino_total
from matriz_distancia import mostrar
from mostrar_cadastro import mostrar_cadastro
from cadastro import cadastro
from limpa_tudo import limpatela
def tela_inicial(entregas, codigo,região_de_origem,destino_final):
    print("""            Longvast-Sistema Inteligente de Gerenciamento de Entregas
1. Cadastrar entrega
2. Listar entregas
3. Consultar entrega
4. Exibir fila de despacho
5. Iniciar transporte
6. Finalizar entrega
7. Exibir matriz de distâncias
8. Exibir estatísticas   
9. Calcular percurso recursivamente
10. Encerrar sistema""") 
    codigo_texto = input("Qual a sua escolha: ")
    while  not codigo_texto.isdigit() or int(codigo_texto) < 1 or int(codigo_texto) > 10:
        print("Escolha Invalida!")
        codigo_texto=input("Qual a sua escolha: ")
    escolha= int(codigo_texto)
    if escolha == 1:
        limpatela()
        região_de_origem,destino_final, entregas, codigo = cadastro(região_de_origem,destino_final,entregas, codigo)
    elif escolha==2:
        limpatela()
        mostrar_cadastro(entregas)
    elif escolha == 7:
        limpatela()
        região_de_origem,destino_final,destino=destino_total(região_de_origem,destino_final,destino)
        mostrar()
    elif escolha==10:
        limpatela()
        print("Adeus!!!")

    return escolha, entregas, codigo, região_de_origem, destino_final
