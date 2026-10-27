
regioes = ["Centro", "Norte", "Sul", "Leste", "Oeste"]
def destino_total(região_de_origem,  destino_final):
    matriz_distancias = [
        [0, 12, 15, 10, 14] ,#"Centro"
        [12, 0, 25, 18, 20] ,  #"Norte",
        [15, 25, 0, 16, 19] ,  #"Sul",
        [10, 18, 16, 0, 22] ,  #"Leste",
        [14, 20, 19, 22, 0] ,#"Oeste"
    ]
    distancias=matriz_distancias[região_de_origem][destino_final]
    return distancias

def mostrar():
        print("======= MATRIZ DE DISTÂNCIA ==============")
        print("""Centro  Norte  Sul  Leste  Oeste
    0        12    15    10    14    Centro
    12       0     25    18    20    Norte
    15       25    0     16    19    Sul
    10       18    16    0     22    Leste
    14       20    19    22    0     Oeste""")
        opcao=input("Só selecionar ENTER!!")
