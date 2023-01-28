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


#1 - Lambda + List.Sort + Sorted
##1.1 - Example List Sort
listA = [5,4,5,9,52,14,12,6,99]
listA.sort()
print(listA)
##1.2 - Example Dictionary Sort
###1.2.1 - Example Dictionary Sort by Key
listB = [
        {'name': 'Jair', 'age': 30, 'city': 'São Paulo'},
        {'name': 'João', 'age': 20, 'city': 'Rio de Janeiro'},
        {'name': 'Maria', 'age': 25, 'city': 'São Paulo'}
        ]
###1.2.2 - function to sort by value
def sortList(item):
    return item['name']
###1.2.3 - changing listB to sort by value
listB.sort(key=sortList)
###1.2.4 - printing listB in order by name
def printList(item):
    for item in listB:
        print(item) #Output: Sorted by Name

##1.3 - Using Lambda to sort by name (the same variable listB)
l1 = sorted(listB, key=lambda item: item['name'])
l2 = sorted(listB, key=lambda item: item['age'])
###1.3.1 - Printing listB in order by name using the printList function
printList(l1)
printList(l2)

#2 - Lambda
##2.1 - Creating a function to execute Lambda
def execute(function, *args): #this line is a function named 'execute' that receive a function and arguments
    return function(*args) #this line print the result of the function
##2.2 - Example of Function
def sum(x, y):
    return x + y
##2.3 - Example of Lambda
print(
    execute(
        lambda x, y: x + y, #This line is a lambda function that receive x and y and return x + y
        2, 3
    ),
    execute(sum(2, 3)), #This line is executing the function sum(2, 3) using the 'execute' function
    sum(2, 3)
)

#3 - Packing and Unpacking using Dictionaries
#3.0 - Simple Example
a,b = 1,2
a,b = b,a
print(a,b) #Return 2,1
#3.1 - Packing and Unpacking using Dictionaries
person = {'name': 'Jair', 'age': 30, 'city': 'São Paulo'}
(a1, b1, c1) = person.items()
print(a1, b1, c1) #Return ('name', 'Jair') ('age', 30) ('city', 'São Paulo')
#3.3 - Joining Dictionaries
person = {'name': 'Jair', 'age': 30, 'city': 'São Paulo'}
personComplementar = {'Dct': '123456', 'Job': 'System Analisys'}
fullPerson = {**person, **personComplementar}
print(fullPerson)
#3.4 - Packing and Unpacking using *Args and **Kwargs
def allArguments(*args, **kwargs):
    print('Not Named Arguments: ', args)
    print('Named Arguments: ', kwargs)
#3.5 - Packing and Unpacking using *Args and **Kwargs
    for key, value in kwargs.items():
        print(f'{key} = {value}')
#3.6 - configDic is a Dictionary that will be unpacked using **kwargs
configDic = {'arg1':1, 'arg2':2, 'arg3':3}
#3.7 - allArguments is a function that receive *args and **kwargs
allArguments(**configDic)

#4 - Using *Args and **Kwargs to packing and unpacking
##4.1 - Joining Dictionaries to understand the concept
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dictAll = {**dict1, **dict2}    #This line is joining the dictionaries
##4.2 - Using Kwarg to unpacking the dictionary
def funcGeneric(arg1, arg2, **kwargs):
    print(arg1, arg2)
    print(**kwargs)
def funcGeneric2(a, b):
    print(a, b)
funcGeneric(1,2, a= 3, b= 4) #Result of print is 1 2 and 3 4

#***********************************************************
#Packing a Tuple
varName = {'name': 'Mary', 'Age': 17, 'Classm': 'First'}
#Unpacking a Tuple
name, age, Classm = varName.values()
print(name)
print(age)
print(Classm)

#***********************************************************
#Using Function and double asterisk
def packAndUnpack(name2, Age2, Classm2):
    print(name2)
    print(Age2)
    print(Classm2)
#Packing Using Tuple
varName2 = {'name2': 'Mary', 'Age2': 17, 'Classm2': 'First'}
#Unpacking Using Tuple and double asterisk in a function
packAndUnpack(**varName2)

#***********************************************************
#List Comprehension
list1 = [1, 2, 3]
list2 = [4, 5, 6]
pairs = [(x, y) for x,y in zip(list1, list2)]
print(pairs)

#***********************************************************
#Mapping Data List
numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squreList = [x**2 for x in numberList]
print(squreList)
#Another Example using Dictionary and List
product = [
    {'Product': 'Egg', 'Value': 10},
    {'Product': 'Meat', 'Value': 20},
    {'Product': 'Onion', 'Value': 15}
    ]
adjustPrice = [x['Value']*1.20 for x in product]
print(adjustPrice)
#Another Example using Lambda
adjustUsingLambda = map(lambda x: x['Value']*1.20, product)
print(list(adjustUsingLambda))
#Filtering Data using list comprehension
filteredProduct = filter(lambda x: x['Product'] == 'Egg', product)
print(list(filteredProduct))