import os,time
import json

print("**************************************")
print("*            MUNDO LIBRO             *")
print("**************************************")
print("[1] - Mantenedor de autores")
print("[2] - Reportes")
print("[3]- Salir")

menuopc = int(input("Donde quiere ingresar: "))

if menuopc == 1:
    print("**************************************")
    print("*         MANTENEDOR AUTORES         *")
    print("**************************************")
    print("[1] - Agregar autor")
    print("[2] - Editar autor")
    print("[3] - Eliminar autor")
    print("[4] - Buscar autor")
    print("[5] - Salir")
    mantenedoropc = int(input("Que quiere hacer: "))
    
    def agregar_autor(nombre, pais):
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
        with open("biblioteca.json","w") as prueba:
            imprimir = json.dump(datos,prueba)


    def editar_autor(ID,Nombre,pais):
        with open("biblioteca.json", "r") as ArchivoBiblio:
            datos= json.load(ArchivoBiblio)
            print(datos["Autor"])
            

    def eliminar_autor(ID):
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

    def buscar_autor(ID): 
        lista=[]
        with open("biblioteca.json", "r") as ArchivoBiblio:
            datos= json.load(ArchivoBiblio)

            for i in datos["Autor"]:
                lista.append(i)
            #ID = int(input("Ingrese el ID del autor"))
            ids = ID - 1
            print(lista[ids])


    if mantenedoropc == 1:
        nombre= input("Ingrese el nombre del autor")
        pais= input("Ingrese el pais del autor")

        agregar = agregar_autor(nombre,pais)
        print(agregar) 
    elif mantenedoropc == 2:
        ID = input("Ingrese el ID del autor")

        eliminar = eliminar_autor(ID)
        print(eliminar) 
    elif mantenedoropc == 3:
        print()
    elif mantenedoropc == 4:
        ID = int(input("Ingrese el ID del autor"))

        buscar = buscar_autor(ID)
        print(buscar) 
    elif mantenedoropc == 5:
        print("Saliendo")
        os.system("cls")
        
if menuopc == 2:
    librosprestados = []
    print("**************************************************")
    print("* AUTOR           CANTIDAD DE LIBROS PRESTADOS   *")
    print("**************************************************")
    librosprestados = []
    with open("biblioteca.json", "r") as ArchivoBiblio:
        datos= json.load(ArchivoBiblio)
        
        for i in datos["Prestamo"]:
            print(i)
            print(i["PrestamoID"], i["LibroID"])
            
 


if menuopc == 3:
    os.system("cls")

