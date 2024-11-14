'''
Reto - IVA 
Un cliente de una empresa de asesoramiento, te han dado una imágen para crear un programa para calcular IVA.
Además, necesitan un informe histórico mostrando todos los datos que han introducido los clientes en su
calculadora (por ejemplo, Mario hizo un cálculo con 45 euros, Ana hizo con 31 euros, …)
https://www.impulsa-empresa.es/calculadora-iva/

Hay que entregar: 
Programa de Python
Código para comprobar (test)
Breve descripción para el cliente (manual de uso), descripción de los retos y mejoras que habéis podido
experimentar trabajando en equipo. Incluir algunas mejoras que has podido hacer.
Descripción de un caso de historia - COMO, QUIERO, PARA QUE
Hay que entregar esta actividad al profesor a través de un vínculo de github

Si te interesa markdown, leer el artículo (traducido al castellano)
'''
import os
from datetime import datetime

os.system('cls')

# registros
cuando = ['2024-11-13 17:34:15.049062','2024-11-13 17:34:16.049063'] # El formato que devuelva python
quien = ['manolo','juan'] # strings
que = ['+','-'] # +-?
cuanto = [123.0,234.0] # son float 
ivaLog = [12,23] # ajustado a int y asumiendo que es %

while True:
    nombre=input("en primer lugar dame tu nombre: ")
    # Obtener la fecha y hora actuales
    now = datetime.now()

    opcion=input("Calculadora IVA: '+' sumar, '-' quitar, '?' visualizar log:  opcion?> ")
    
# sumar IVA
    if opcion=='+':
        valor=float(input("Ok, a que cantidad quieres añadir IVA?> "))
        iva=int(input("que % de IVA quieres sumar?> "))
        resultado = valor + valor * iva/100
        print(f"La cantidad inluyendo IVA es: {resultado:.2f}")

# quitar IVA
    elif opcion=='-':
        valor=float(input("Ok, a que cantidad quieres quitar IVA?> "))
        iva=int(input("que % de IVA quieres quitar?> "))
        resultado = valor * 100/(100+iva)
        print(f"La cantidad quitando el IVA es: {resultado:.2f}")
        pass # aqui añadir el log

# Visualizar Log
    elif opcion=='?':
        valor="***"
        iva="***"
        print("*** Este es el Log, muchacho: ***")
        for i in cuando:
            print(f" > {i}: {quien[cuando.index(i)]}, realizó la operacion {que[cuando.index(i)]}\
                por la cantidad {cuanto[cuando.index(i)]} e IVA de {ivaLog[cuando.index(i)]} %")
        print("*** Fin del LOG *** ")

# Error
    else:
        valor="***"
        iva="***"
        print("Opcion no existente")

    # finalmente Registramos
    quien.append(nombre)
    cuando.append(now)
    que.append(opcion)
    cuanto.append(valor)
    ivaLog.append(iva)
       
