# Gerenciamento simples de estoque com Listas
estoque = ["Celular", "Fone", "Carregador"]

# Adicionando e removendo de forma segura
if "Fone" in estoque:
    estoque.remove("Fone")
    estoque.append("Fone Bluetooth")

quantidade_total = len(estoque)
print(f"Itens no estoque ({quantidade_total}): {estoque}")
