
import matplotlib.pyplot as plt
import pandas as pd
import os

#Função para ler apenas letras:
def leiastr(msg):
    while True:
        print()
        verif=str(input(msg).strip().replace(" ", ""))
        if verif.isalpha() == False:
            print()
            print("ERRO:""\nDigite apenas letras.")
            continue
        else:
            verif=verif.lower()
            return verif


def conferexist():
    
    global plan
    global planpart
    global x

    while True:
        file_path = os.path.join(str(plan)+".xlsx")
        try:
            x=pd.read_excel(file_path, str(planpart))
        except (FileNotFoundError, ValueError, Exception):
            print()
            print("Essa planílha não existe.\n\nTente novamente.")
            print()
            plan=input("Digite o nome da planílha: ")
            print()
            planpart=input("Digite o nome do compartimento desejado: ")
            continue
        else:
            break


def seeplan():
    
    conferexist()
    
    newcolname=[]

    for elem in x:
        elem=str(elem)
        x.update(x[elem].fillna('   '))
        if 'nan' in elem or 'Unnamed' in elem:
            newcolname.append('     ')
        else:
            newcolname.append(str(elem))
    x.columns = newcolname
    
    return x
    

def run():
    global plan, planpart, x

    reboot='s'
    while 's' in reboot:
        os.system("cls")
        print()
        plan=input("Digite o nome da planílha: ")
        print()
        planpart=input("Digite o nome do compartimento desejado: ")
        x=0
        seemorepart='s'
        while 's' in seemorepart:
            os.system("cls")
            print(seeplan())
            seemorepart=str(f"Deseja ver mais alguma compartimento da planílha: {plan}? ")
            seemorepart=leiastr(seemorepart)
            if 's' in seemorepart:
                print()
                planpart=input("Digite o nome do compartimento desejado: ")
        reboot=str("Deseja reiniciar o programa? ")
        reboot=leiastr(reboot)
    input()


run()