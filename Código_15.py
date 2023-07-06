# Em loops:

import time
from datetime import datetime, timedelta

#for i in range(10):
    #print(i+1)

#for i in "Bro code":
    #print(i)

#for seconds in range(10,0,-1):
    #print(seconds)
    #time.sleep(1)
#print("Feliz ano novo!")



def temporizador(minutos, segundos):

    tempo_inicial = datetime.now()

    tempo_final = tempo_inicial + timedelta(minutes=minutos, seconds=segundos)


    while datetime.now() < tempo_final:

        tempo_restante = tempo_final - datetime.now()

        tempo_formatado = tempo_restante - timedelta(microseconds=tempo_restante.microseconds)

        print(tempo_formatado, end=".")

        time.sleep(1)

print("você passou a noite dos coisas ruim! >:-D")

temporizador(4, 30)



