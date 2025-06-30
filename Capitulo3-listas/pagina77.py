# 29 de junho de 2025
# Domingo, noite fria

# Página 77 - Removendo um item com o método POP()

print("Removendo um item com o método POP()")
motorcycles = ['honda', 'yamaha', 'suzuki']
print("Lista original:")
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print("Lista com o último valor excluido:")
print(motorcycles)
print("O valor exlcuido:")
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("\nThe last motorcycle I owned was a " + last_owned.title() + ".")