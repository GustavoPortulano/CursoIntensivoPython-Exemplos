# 29 de junho de 2025
# Domingo, noite fria

# Página 77 - Removendo itens de qualquer posição em uma lista

print("\nRemovendo itens de qualquer posição em uma lista")

mortorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = mortorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

# Removendo um item de acordo com o valor
print("\nRemovendo um item de acordo com o valor.")
mortorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(mortorcycles)
print("Removendo o último valor da lista:")
mortorcycles.remove('ducati')
print(mortorcycles)

print("\nNova mensagem")
mortorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = "ducati"
mortorcycles.remove(too_expensive)
print(mortorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

