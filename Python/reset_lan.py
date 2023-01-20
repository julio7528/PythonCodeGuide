import io
import subprocess
from datetime import datetime
import os

def log(message):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    with open(f'{file}.txt', 'a+') as f:
        f.write('\n****************************\n')
        f.write(f'\nLog:{dt_string} - {message}\n')

def commandP(command):
    output = subprocess.getoutput(command)
    return output

def recordV(file, output):
    with io.open(f'{file}.txt', 'a+') as f:
        f.write(output)

#Verificando Arquivo e criando
now = datetime.now()
dt_string = now.strftime("%d-%m-%Y")
file = 'Report - ' + dt_string
file_exists = os.path.exists(f'{file}.txt')
if file_exists:
    os.remove(f'{file}.txt')

listLog = ['Iniciando Consulta do Ping\n','Comando ipconfig /release\n','Comando ipconfig /renew\n','Comando ipconfig /flushdns\n']
listCommand = ['ping www.google.com','ipconfig /release','ipconfig /renew','ipconfig /flushdns']
counter = int(0)

for i in listLog:
    log(listLog[counter])
    output = commandP(listCommand[counter])
    recordV(file, output) 
    counter += 1
