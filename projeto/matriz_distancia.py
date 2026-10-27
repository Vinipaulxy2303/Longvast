regioes = ["Centro", "Norte", "Sul", "Leste", "Oeste"]

matriz_distancias = [
    [0, 12, 15, 10, 14],   # Centro
    [ 12, 0, 25, 18, 20],   # Norte
    [  15, 25, 0, 16, 19],   # Sul
    [10, 18, 16, 0, 22],   # Leste
    [14, 20, 19, 22, 0]    # Oeste
]

def mostrar():
    for linha in matriz_distancias:
        print(*linha)
    opcao=input("Só selecionar ENTER!!")
