

UrbanoMt2 = 25000
Permiso_urbano = 0.45
ComercialMt2 = 60000
Permiso_comercial = 0.75
CampestreMt2 = 35000
Permiso_campestre = 0.15

ls_urbano = []
ls_comercial = []
ls_campestre = []

import os

def fnt_limpiar():
    os.system('cls')
    print('Autor: Valentina Arias Raigosa.')
    print('Fecha: 25 de abril del 2024\n')

def fnt_registrar(nombre, ancho, largo, tipo_lote):
    if tipo_lote == "Urbano":
        valor_mt2 = UrbanoMt2
        permiso_construccion = Permiso_urbano
    elif tipo_lote == "Comercial":
        valor_mt2 = ComercialMt2
        permiso_construccion = Permiso_comercial
    elif tipo_lote == "Campestre":
        valor_mt2 = CampestreMt2
        permiso_construccion = Permiso_campestre

    area = ancho * largo
    valor_lote = area * valor_mt2
    valor_permiso = valor_lote * permiso_construccion
    print(f'El valor del lote es: {valor_lote:.2f}')
    print(f'El valor del permiso de construcción es: {valor_permiso:.2f}')
    print(f'El valor total es: {valor_lote + valor_permiso:.2f}')

def fnt_selector(op):
    global sw
    fnt_limpiar()
    if op == '1':
        nombre = input('Nombre: ')
        ancho = float(input("Ingrese el ancho del lote (en metros): "))
        largo = float(input("Ingrese el largo del lote (en metros): "))
        tipo_lote = input('>>>>MENU DE LOTES<<<<\n1. Urbano\n2. Comercial\n3. Campestre\n-> ')
        if tipo_lote == "1":
            tipo_lote = "Urbano"
            R = {'nombre': nombre, 'Area': ancho * largo, 'Tipo de lote': tipo_lote}
            ls_urbano.append(R)
        elif tipo_lote == "2":
            tipo_lote = "Comercial"
            R = {'nombre': nombre, 'Area': ancho * largo, 'Tipo de lote': tipo_lote}
            ls_comercial.append(R)
        elif tipo_lote == "3":
            tipo_lote = "Campestre"
            R = {'nombre': nombre, 'Area': ancho * largo, 'Tipo de lote': tipo_lote}
            ls_campestre.append(R)
        fnt_registrar(nombre, ancho, largo, tipo_lote)
        enter = input('<ENTER>')
    elif op == '2':
        fnt_limpiar()
        print('Lotes Urbanos:')
        for lote in ls_urbano:
            print(lote)
        print('Lotes Comerciales:')
        for lote in ls_comercial:
            print(lote)
        print('Lotes Campestres:')
        for lote in ls_campestre:
            print(lote)
        enter = input('Presione <ENTER> para continuar')
    elif op == '3':
        sw = False

sw = True
while sw == True:
    fnt_limpiar()
    op = input('\n\n>>>>MENU PRINCIPAL<<<<\n1. Registrar Lote\n2. Mostrar Lotes\n3. Salir\n-> ')
    fnt_selector(op)