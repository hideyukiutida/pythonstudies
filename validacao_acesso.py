# Exemplo de Lógica de Acesso e Cupons (Clean Code)
convidados = ["Ana", "Bia", "Caio"]
nome_na_porta = "Caio"

# Escrita enxuta que aprendi:
acesso_proibido = nome_na_porta not in convidados
status = "Entrada Negada" if acesso_proibido else "Bem-vindo!"

print(f"Status do convidado: {status}")
