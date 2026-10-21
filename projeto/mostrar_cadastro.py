from mostrar_cadastro import entregas
def mostrar_cadastro():
    for chave, valor in entregas.items():
        print(f"{chave}: {valor}")
    print("-" * 30)