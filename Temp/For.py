import os
import platform

def limpar_tela():
    # Verifica se o sistema é Windows para usar 'cls' ou 'clear' para outros (Linux/macOS)
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Exemplo de uso
"""
print("Conteúdo antigo...")
limpar_tela()
print("Tela limpa.")   
"""

limpar_tela()

numeros = [1, 2, 3, 4, 5]
numeros.append(6)
for numero in numeros:
    print(numero)
