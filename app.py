# Exercício 1 Faça um algoritmo usando o for para mostrar os números pares e impares de 0 a 100.
for n in range(101):
  if n % 2 == 0:
    print("O número ", n, "é par")
  else:
    print("O numero", n, "é impar")


# Exercício 2 Escreva um script que leia três números e mostre o maior e o menor deles.
nume1 = float(input("Digite o primeiro número: "))
nume2 = float(input("Digite o sengundo número: "))
nume3 = float(input("Digite o terceiro número: "))

maior = nume1
menor = nume1

if nume2 > maior:
   maior = nume2

if nume2 < menor:
   menor = nume2

if nume3 > maior:
   maior = nume3

if nume3 < menor:
   nume3 = menor

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

# Exercício 3 Faça um algoritmo que imprima o nome digitado pelo usuário na vertical em escada. Exemplo: F FU FUL FULA FULAN FULANO

nome = input("Digite um nome")
escada = ""
for letra in nome:
  escada += letra
  print(escada)

# Exercício 4 A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... (o próximo termo, a partir do terceiro (número 2), é sempre gerado a partir do somatório dos últimos dois). Faça um programa capaz de gerar a série até o n−ésimo termo (onde o valor n deve ser inserido pelo usuário).

n = int(input("Digite o valor de n (número de termos): "))
a, b =1, 1

if n >= 1:
  print(a)

if n <= 2:
  print(b)

for i in range(3, n + 1):
  proximo = a + b
  print(proximo)
  a, b = b, proximo

 #Exercício 5 Faça um programa que leia e valide as seguintes informações:Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite o nome (mais de 3 caracteres): ")
while len(nome) <= 3:
  print("Erro: O nome deve ter mais de 3 caracteres.")
  nome = input("Digite novamente a nome: ")

idade = int(input("Digite a idade (entre 0 a 150): "))
while idade < 0 or idade > 150:
  print("Erro: A idade deve estar entre 0 a 150.")
  idade + int(input("Digite novamente a idade: "))


salario = float(input("Digite o salário (maior que zero): "))
while salario <= 0:
  print("Erro: O salário deve ser maior que zero.")
  salario = float(input("Digite novamente o salário: "))

sexo = input("Digite o sexo ('f' ou 'm'): ").lower()
while sexo != 'f' and sexo != 'm':
  print("Erro: Opção invalida, digite apenas 'f' ou 'm'.")
  sexo = input("Digite novamente o sexo: ").lower()

estado_civil = input("Digite seu estado civil ('s', 'c', 'v', 'd'): ").lower()
while estado_civil not in ['s', 'c', 'v', 'd']:
  print("Erro; Opção invalida. Use apenas: 's', 'c', 'v', 'd.")
  estado_civil = input("Digite novamente o estado civil: ").lower()

print("\n--- Cadastro realizado com sucesso! ---")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R$ {salario:.2f}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")

# Exercício 6: Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1. Dica: Utilize o operador aritmético %, que retorna o resto da divisão de dois números.

num = int(input("Digte um número inteiro: "))

cont_divisores = 0

for i in range(1, num + 1):
  if num % i == 0:
    cont_divisores = cont_divisores + 1
if cont_divisores == 2:
  print(f"O número {num} é primo!")
else:
  print(f"O número {num} não é primo.")

# Exercício 7 Faça um algoritmo utilizando o laço FOR que descreva o Fatorial de um número digitado pelo usuário.

num = int(input("Digite o numero fatórial: "))
fatorial = 1
if num < 0:
  print("não é fatorial")
elif num == 0:
  print("O fatorial de 0 é 1.")
else:
  for i in range(1, num + 1):
    fatorial = fatorial * i
  print(f"O fatorial de {num} é {fatorial}")

  #Exercício 8 Dada a lista L = [5, 7, 2, 9, 4, 1, 3] Escreva um programa que imprima as seguintes informações: a) tamanho da lista. b) maior valor da lista. c) menor valor da lista. d) soma de todos os elementos da lista. e) lista em ordem crescente. f) lista em ordem decrescente.

  L = [5, 7, 2, 9, 4, 1, 3]

tamanho = len(L)
print(f"a) Tamanho da lista: {tamanho}")

maior = max(L)
print(f"b) Maior valor: {maior}")

menor = min(L)
print(f"c) Menor valor: {menor}")

soma = sum(L)
print(f"d) Ordem crescente: {soma}")

crescente = sorted(L, reverse=True)
print(f"e) Ordem crescente: {crescente}")

# Exercício 9 Dada a tabela em anexo , crie um dicionário que a represente.

lanchonete = {
    "salgado": 4.50,
    "Lanche": 6.50,
    "Suco": 3.00,
    "Refrigerante": 3.50,
    "Doce": 1.00
}
print(lanchonete)

#Exercício 10 Utilizando o laço While faça um programa que peça uma senha ao usuário, e que imprima "Acesso liberado" apenas se o usuário digitar a senha corretamente. A senha devera ser a seguinte senha númerica : "676767".

senha_correta = "676767"

senha_digitada = ""

while senha_digitada != senha_correta:
  senha_digitada = input("Digite a senha : ")
  if senha_digitada != senha_correta:
    print("Senha incorreta! Tente novamente")
print("Acesso liberado")

# Exercício 11 Escreva um programa que peça um número de 1 a 10, e mostre a tabuada desse número.
num = int(input("Digite um número de 1 a 10 para ver a tabuada: "))

if num < 1 or num > 10:
  print("Número inválido! Digite apenas entre 1 e 10")
else:
  print(f"Tabuada do {num}:")

  for i in range(1,11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")






