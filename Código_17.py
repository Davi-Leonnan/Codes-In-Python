# Mover um arquivo:


import os

source = "Bro_Code_Guide"
destination = "C:\\Dionisio_N (D:)\\Documentos de Davi (DDD)\\_____Códigos_____\\Bro_Code_Guide"

try:
    if os.path.exists(destination):
        print("There is already aq file there!")
    else:
        os.replace(source,destination)
        print(source+" Was moved")
except FileNotFoundError:
    print(source+" Was not found")
