import json

def agregar_autor(nombre, pais):#B
    diccionario = {
        "AutorID": 1, #DUDAS
        "Nombre": nombre,
        "Nacionalidad": pais
    }
    #datos["Autor"].append(diccionario, ArchivoBiblio, indent=4)
    print(len(diccionario))

    with open("biblioteca.json", "r") as ArchivoBiblio:
        datos= json.load(ArchivoBiblio)
        print(datos["Autor"])
    
    datos["Autor"].append(diccionario)
    print(datos["Autor"])
    with open("aaa.json","w") as prueba:
        imprimir = json.dump(datos,prueba)


def editar_autor(ID,Nombre,pais):#M
    with open("biblioteca.json", "r") as ArchivoBiblio:
        datos= json.load(ArchivoBiblio)
        print(datos["Autor"])
        

def eliminar_autor(ID):#M
    lista=[]
    diccionario = {
        "AutorID": None, #DUDAS
        "Nombre": None,
        "Nacionalidad": None
    }
    #datos["Autor"].append(diccionario, ArchivoBiblio, indent=4)

    with open("biblioteca.json", "r") as ArchivoBiblio:
        datos= json.load(ArchivoBiblio)
        print(datos["Autor"])
        for i in datos["Autor"]:
            #if i["ID"] == ID :
            #print(i)
            lista.append(i)
            print(lista[0])

            if lista[0] == ID :
                print(lista[0])
            #print(datos["Autor"])

        with open("biblioteca.json", "r") as ArchivoBiblio:
            datos= json.load(ArchivoBiblio)
            print(datos["Autor"]) 


def buscar_autor(ID): #B
    lista=[]
    with open("biblioteca.json", "r") as ArchivoBiblio:
        datos= json.load(ArchivoBiblio)

        for i in datos["Autor"]:
            lista.append(i)
        #ID = int(input("Ingrese el ID del autor"))
        ids = ID - 1
        print(lista[ids])