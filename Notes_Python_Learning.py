"""
Title: Python Lessons
Developer: Júlio Gomes
Date created: 11/2022
"""

''' First Step print with comments '''

# Print a Text
# \r\n -> CRLF
# \n -> LF
print("Test", 1, "Delimitator", sep="-", end='\nEnd of line\n')

#Notation in a string using ''
print("Notation 'in' a string")

#Type in a string
print(type(12),type(1.2),type("abc"),type(True))

#Boolean type in a string
print(10 == 10)
print(type(False == False))

#Converting numbers and strings
print(float('1') + 1)
print(str(11) + 'b')

#Using variables
varInt = 4 #is a variable integer
varStr = 'Jacob' #is a variable string
varBool = varInt <= 18 #is a variable boolean
print("User:",varStr, varInt,"Years - Underage:",varBool, sep=" ",end=".\n")

#Calculating and using input
var1 = input('Digite n1: ')
var2 = input('Digite n2: ')
n1 = int(var1)
n2 = int(var2)
print("Sum", n1+n2,"Subtract",n1-n2,"Multiply",n1*n2,"Divide",n1/n2, sep=" ")
print("Int Division", n1//n2,"Exponentiation",n1**n2,"Module",n1%n2, sep=" ")

#Concat String and Multiply5
n1 = 5
n2 = "python"
print((str(n1)+n2)*n1)
print(n2 * n1)

#Ord                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ering Calculation functions
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)

#Layout for print
nome = "Name"
idade = 23
formato = f'{nome} have {idade:.2f} years old'
print(formato)

#If statement
idade0 = input('Type an age ')
idade = int(idade0)
if idade < 18:
    print('Underage')
elif idade >=18:
    print('Majority age')
else:
    print('Format input not allowed.')

#Relational operators
var1 = input('Digite n1: ')
var2 = input('Digite n2: ')
n1 = int(var1)
n2 = int(var2)
print('n1 diferente n2 ',n1 != n2)
print('n1 igual n2 ',n1 == n2)
print(n1>n2 and n2!=n1)
print(n1>n2 or n2!=n1)
print(not n2!=n1)

#Bool using OR statement - 1 true and 0 false
variavel_a = 1 or 0
variavel_b = 0 or 1
print(bool(1), bool(0))

#In Statement
nome =input('digite nome ')
if 'o' in nome:
    print(f'O nome {nome} usa o.')
else:
    print(f'O nome {nome} NÃO usa o.')

#Not In Statement
nome =input('digite nome ')
if 'o' not in nome:
    print(f'O nome {nome} sem uso do o.')
else:
    print(f'O nome {nome} não pode usar o.')

#Interpolation for strings
"""
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))

#Formating a string
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')

#Split the string
var1 = 'a simple text'
print(var1[2:9:1])
#Invert the string
var1 = 'a simple text'
print(var1[::-1])

"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')


#Is, Not Is and None
condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if is None)

#replace value in a variable
nome = "joao da silva"
outra_variavel = nome
outra_variavel = f'{outra_variavel[:3]}ABC{outra_variavel[4:]}'
print(outra_variavel)

#Function returning variables

def funcao(valor1, valor2):
    print(valor1, valor2)
    resultado = valor1 + valor2
    return resultado

resultadoFora = funcao(10, 10) #every function need be called in a variable

print(resultadoFora)

#Function Using Arguments

def funcao(*args): #using arguments executing a function - like print
    for i in args:
        print(i)
funcao(10,20,30,40,50,60)

def funcao2(*args): #using arguments using a return
    resultado = 0
    for i in args:
        resultado = resultado + i
    return resultado
resultadoFora = funcao2(10,20,30,40,50)
print(resultadoFora)
        
    
"""
Higher Order Functions
Funções de primeira classe
"""
def soma(*args):
    resultado=0
    for i in args:
        resultado = resultado + i
    print(resultado)
    return resultado

def somar(soma, *args): #Está chamando a função soma dentro de outra função
    print('terminou')

somar(soma(10,20,30,40)) #Quando executar, o resultado será o valor da soma e depois o print

"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))

#Multiplicação usando Closure
def multiplicador(numero):
    def valor(quantidade):
        i = 1
        quantidade += 1
        while i < quantidade:
            resultado = numero * i
            print(f'{resultado} = {numero} * {i}')
            i += 1
            if i < (quantidade):
                continue
            else:
                return resultado
    return valor

multiplicacao = multiplicador(2)

multiplicacao(10)

#CRUD by Dictionary
def cadastrar():
    nome = input("Digite o Nome: ")
    sobrenome = input("Digite o Sobrenome: ")
    lista = {
        'nome': nome,
        'sobrenome': sobrenome,
        }
    return lista

cadLista = cadastrar()

cadPessoa = {
    'Nome': cadLista['nome'],
    'Sobrenome': cadLista['sobrenome'],
}

def imprimir():
    print("Nome: " + cadPessoa['Nome'])
    print("Sobrenome: " + cadPessoa['Sobrenome'])

imprimir()

print(f"Len of List: {cadPessoa.__len__()}")

print(f"Keys {cadPessoa.keys()}")
for keyOne in cadPessoa.keys():
    print(f"List of Keys: {keyOne}")

print(f"Values {cadPessoa.values()}")
for keyOne in cadPessoa.values():
    print(f"List of Values: {keyOne}")

for chave,valor in cadPessoa.items():
    print("Print by key and value:")
    print(f"{chave}: {valor}")

print(f"Printing name by get: {cadPessoa.get('Nome')}")

cadPessoa.update({'Nome': "Jair",
                  'Sobrenome': "Moises"
                  })

print(cadPessoa)

