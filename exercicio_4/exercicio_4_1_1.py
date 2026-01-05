# Exercicio 4.1.1
print("Escolha o que deseja comprar:")
print("1 Maçã")
print("2 Laranja")
print("3 Banana")
# Entrada do usuário
produto = int(input("Qual sua escolha? "))
qtd = int(input("Quantas unidades? "))

# Verificação do produto e cálculo do total
if produto == 1:
    pagar = qtd * 2.3
    print(f"Você comprou {qtd} maçã(s). Total a pagar: R${pagar:.2f}")
elif produto == 2:
    pagar = qtd * 3.6
    print(f"Você comprou {qtd} laranja(s). Total a pagar: R${pagar:.2f}")
elif produto == 3:
    pagar = qtd * 1.85
    print(f"Você comprou {qtd} banana(s). Total a pagar: R${pagar:.2f}")
else:
    print("Produto inexistente!")
