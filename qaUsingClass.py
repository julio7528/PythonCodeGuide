
import os
class Questionario:

    def __init__(self, lista):        
        self.lista = lista 
        
    def calcular(self):

        notaAcerto = 0

        os.system('cls' if os.name=='nt' else 'clear')

        for item in self.lista:

            def imprimePerguntas(item):
                print(f"{item['Pergunta']}")

            def digitaResposta():
                vResposta = input('Digite a Resposta: ')
                return vResposta

            def imprimeAlternativas(item):
                for i, keyOne in enumerate(item['Opções']):                                        
                    print(f"Alternativa {i+1}: {keyOne}")

            def avalliaQuestao(item, vResposta):
                avaliacao = ""   
                for i, keyOne in enumerate(item['Opções']):
                    if vResposta == keyOne:
                        avaliacao = "Você Acertou"            
                    else:
                        if avaliacao == "Você Acertou":
                            continue
                        avaliacao = "Você Errou"
                return avaliacao

            imprimePerguntas(item)            
            imprimeAlternativas(item)
            resposta = digitaResposta()
            avaliacao = avalliaQuestao(item, resposta)
            if avaliacao == "Você Acertou":
                notaAcerto += 1
                print(f"{avaliacao} 👍")
            else:
                print(f"{avaliacao} ❌")
            
            print("\n***************\n")

        if notaAcerto < (self.lista.__len__()*0.7): 
            situacao = "REPROVADO!"
        else:
            situacao = "APROVADO!"
        print(f"Boletim: Você Acertou {notaAcerto} de {self.lista.__len__()} - {situacao}")

perguntas =[{
'Pergunta': 'Qual é o elemento mais leve do universo?',
'Opções': ['Ouro', 'Hélio', 'Carbono', 'Prata'],
'Resposta': 'Hélio',
},
{
    'Pergunta': 'Qual é o maior planeta do Sistema Solar?',
    'Opções': ['Mercúrio', 'Júpiter', 'Saturno', 'Terra'],
    'Resposta': 'Júpiter',
},
{
    'Pergunta': 'Qual é a temperatura da superfície do Sol?',
    'Opções': ['-273C', '-80C', '5500C', '-23C'],
    'Resposta': '5500C',
}]

final = Questionario(perguntas)
final.calcular()