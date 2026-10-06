# Variáveis
# nome, celular, endereço ...

velocidade_internet = 1024
print (velocidade_internet)

# Numéros inteiros (int)
idade = 60
# Números decimais (float)
nota = 9.5
# Textos (string) (str)
nome_completo = "Marcio Alves Moreira"
# Booleanos (True ou False) (bool)
pode_entrar = False

print(type(idade))
print(type(nota))
print(type(nome_completo))
print(type(pode_entrar))



# Problema 1 - Valor por Hora
# Escreva um programa que retorna o valor hora de um funcionário
# com base no seu salário mensal e horas trabalhadas por mês.

"""

# Método 5 Qs para montar um algoritimo:

Analise criticamento o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais 
informações/investigue mais até que você mesmo compreenda completamente o problema.)

1. Quais são os dados de entrada necessários?
- Salário Mensal
- Quantidade de horas trabalhadas

2. O que devo fazer pcom estes dados?
-Calcular o valor hora

3. Quais são as restrições deste problema?
- Precisa ter um valor do salário mensal
- Precisa ter um valor da quantidade de horas trabalhadas 

4. Qual é o resultado esperado?
- Exibir o valor hora da pessoa, com base no cálculo de valor hora

5. Qual é a sequência de passos a ser feita para chegar aos resiltado esperado?
(pseudocódigo)
- pegar o valor do salário mensal do funcionário e dividir por 360h (1 mês de trabalho)
- Multiplar este valor hora pela quantidade de horas trabalhadas pelo funionário em determinado mês
- Mostrar o resultado do valor encontrado na tela.

## Lógica do professor
- receber salário mensal
- receber quantidade de horas
- valor hora = salário mensal / quantidade de horas trabalhadas
- exibir valor hora

"""

salario_mensal = input("Qual é o seu salário mensal: ")
horas_trabalhadas = input("Quantas horas você trabalha por mês? ")
valor_hora = float(salario_mensal) / int(horas_trabalhadas)
print(valor_hora)



