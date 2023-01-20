
# #Exercicio de Cadastro
# print("Cadastro\n")
# nome = input("Nome: ")
# idade = input("Idade: ")

# if nome != "":
#     intidade = int(idade)

# validationForm = ((nome != "") and (idade != "")) 
# if validationForm:
#     print(f"Nome: {str(nome)}")
#     print(f"Idade: {str(idade)}")
#     print(f"nome invertido: {nome[::-1]}")

#     if ' ' in nome:
#         print(f'O nome {nome} usa Espaço.')
#     else:
#         print(f'O nome {nome} NÃO usa Espaço.')
    
#     print("o nome contém " + str(len(nome)) + " letras")
#     print("primeira letra " + str(nome[1]))
#     print("ultima letra " + str(nome[-1]))

# else:
#     print("campo faltando")

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# print("Avaliando número")
# varInt = input("Digite um número inteiro: ")

# varIntValidate = (str.isdigit(varInt))

# if varIntValidate:
#     print("It's a Integer number")
#     if (int(varInt)%2) == 0:
#         print("It's an even number")
#     else:
#         print("It's an odd number")
# else:
#     print("It's not a Integer number")
    

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# import re
# print("Programa de saudação")
# varHoras = input("Digite as horas: ")

# r = re.compile('.*:.*')
# if not r.match(varHoras) is not None:
#    print ('error: invalid format time')
#    exit()

# varHorasHoras = int(varHoras[0:2:1])

# if varHorasHoras >= 0 and varHorasHoras <=11:
#     print(f"Good Morning is {varHoras} o clock")
# elif varHorasHoras >= 12 and varHorasHoras <=17:
#     print(f"Good Afternoon is {varHoras} o clock")
# elif varHorasHoras >= 18 and varHorasHoras <=23:
#     print(f"Good Evening is {varHoras} o clock")
# else:
#     print("Time value not allowed")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
# print("Medidor de nome")
# nome = input("digite o nome: ")

# curto = len(nome) <=4
# normal = len(nome) >= 5 and len(nome) <=6
# grande  = len(nome) >= 7

# if curto:
#     print(f"O nome {nome} é curto com {len(nome)} letras")
# if normal:
#     print(f"O nome {nome} é normal com {len(nome)} letras")
# if grande:
#     print(f"O nome {nome} é grande com {len(nome)} letras")

# Questionário usando Classe e Funções
