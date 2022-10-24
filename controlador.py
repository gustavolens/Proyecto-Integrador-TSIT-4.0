import modelo

def ListarAlbumesPorArtistas():
    con = modelo.Conectar()
    listado = con.ListarAlbumes()
    print("\n| COD. ÁLBUM   |          NOMBRE              |       INTERPRETE              |   GENERO   |     DISCOGRAFICA   |   PRECIO   |   CANTIDAD   |  FORMATO   |")
    for album in listado:
        print(' ',album[0],"\t",album[1],"\t\t",album[2]+' '+album[3],"\t\t  ",album[4],"\t",album[5]," $",album[6]," Cant:",album[7]," ",album[8])
    input("Presione ENTER para continuar")

def ListarAlbumesPorGenero():
    con = modelo.Conectar()
    listado = con.ListarPorGenero()
    print("\n| COD. ÁLBUM   |          NOMBRE              |       INTERPRETE              |   GENERO   |     DISCOGRAFICA   |   PRECIO   |   CANTIDAD   |  FORMATO   |")
    for album in listado:
        print(' ',album[0],"\t",album[1],"\t\t",album[2]+' '+album[3],"\t\t  ",album[4],"\t",album[5]," $",album[6]," Cant:",album[7]," ",album[8])
    input("Presione ENTER para continuar")








def InsertarAlbum():
    cod_album = int(input("\nIngrese el código del nuevo Álbum: "))
    nombre = input("Ingrese el nombre del álbum: ")

    # Hay que tener los siguientes datos ya dentro de la base:
    con = modelo.Conectar()

    print("\nIntérpretes Disponibles:")

    for i in con.ListarInterprete():
        print(i)
    print("\n")
    print("En caso de que el Intérprete no esté en la lista, ingrese 0 para agregarlo.")  
  
    id_interprete = int(input("\nIngrese el ID del Intérprete: "))
    if id_interprete == 0:
        nombre = input("Ingrese el nombre del Intérprete: ")
        apellido = input("Ingrese el apellido del Intérprete: ")
        nacionalidad = input("Ingrese la nacionalidad del Intérprete: ")
        foto = input("Ingrese la dirección web de la foto del Intérprete: ")
        nuevoInterprete = modelo.Interprete(0,nombre,apellido,nacionalidad,foto,1)
        con.InsertarInterprete(nuevoInterprete)
        id_interprete = con.ObtenerIDGenerado()
        print("El ID del Intérprete es: ",id_interprete)  
    print("\nGénero")
    for g in con.ListarGenero():
        print(g)
    id_genero = int(input("\nIngrese el ID del Género: "))

    cant_temas = int(input("\nIngrese la cantidad de temas: ")) # Menos este, por supuesto.

    print("\nDiscográfica")
    for d in con.ListarDiscografica():
        print(d)
    id_discografica = int(input("\nIngrese el ID de la discografica: "))

    print("\nFormato")
    for f in con.ListarFormato():
        print(f)
    id_formato = int(input("\nIngrese el ID del formato: "))
    # Hasta acá.

    fec_lanzamiento = input("\nIngrese la Fecha de Lanzamiento (aaaa-mm-dd): ")
    precio = float(input("\nIngrese el precio: "))
    cantidad = int(input("\nIngrese cantidad disponible de este álbum: "))
    caratula = input("\nIngrese la dirección web de la Carátula: ")

    nuevoAlbum = modelo.Album(0,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula)
    con.InsertarAlbum(nuevoAlbum)
    input("Presione ENTER para continuar")

def ModificarAlbum():
    ListarAlbumesPorArtistas()
    cod_album = int(input("\nIngrese el código del Álbum que quiere modificar: "))

    nombre = input("Ingrese el nuevo nombre del álbum: ")

    # Hay que tener los siguientes datos ya dentro de la base:
    con = modelo.Conectar()

    print("\nIntérpretes Disponibles:")

    for i in con.ListarInterprete():
        print(i)
    id_interprete = int(input("\nIngrese el ID del Intérprete: "))
    
    print("\nGénero")
    for g in con.ListarGenero():
        print(g)
    id_genero = int(input("\nIngrese el ID del Género: "))

    cant_temas = int(input("\nIngrese la cantidad de temas: ")) # Menos este, por supuesto.

    print("\nDiscográfica")
    for d in con.ListarDiscografica():
        print(d)
    id_discografica = int(input("\nIngrese el ID de la discografica: "))

    print("\nFormato")
    for f in con.ListarFormato():
        print(f)
    id_formato = int(input("\nIngrese el ID del formato: "))
    # Hasta acá.

    fec_lanzamiento = input("\nIngrese la Fecha de Lanzamiento (aaaa-mm-dd): ")
    precio = float(input("\nIngrese el precio: "))
    cantidad = int(input("\nIngrese cantidad disponible de este álbum: "))
    caratula = input("\nIngrese la dirección web de la Carátula: ")

    nuevoAlbum = modelo.Album(0,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula)
    con.ModificarAlbum(nuevoAlbum)
    input("Presione ENTER para continuar")

def EliminarAlbum():
    ListarAlbumesPorArtistas()
    cod_album = int(input("\nIngrese el código del Álbum que quiere eliminar: "))
    con = modelo.Conectar()
    con.EliminarAlbum(cod_album)
    input("Presione ENTER para continuar")



def InsertarInterprete():
    con = modelo.Conectar()
    print("Estos son los Intérpretes vigentes actualmente:")
    for i in con.ListarInterprete():
        print(i)
    nombre = input("\nIngrese el nombre del Intérprete: ")
    apellido = input("Ingrese el apellido del Intérprete: ")
    nacionalidad = input("Ingrese la nacionalidad del Intérprete: ")
    foto = input("Ingrese la dirección web de la foto del Intérprete: ")
    nuevoInterprete = modelo.Interprete(0,nombre,apellido,nacionalidad,foto,1)#El 1 es para darlo de alta en vigente. Si el vigente es 0 (false) no se mostrará.
    con = modelo.Conectar()
    con.InsertarInterprete(nuevoInterprete)
    input("Presione ENTER para continuar")

def ModificarInterprete():
    con = modelo.Conectar()
    for i in con.ListarInterprete():
        print(i)
    id_interprete = int(input("\nIngrese el ID del Intérprete que quiere modificar: "))
    nombre = input("Ingrese el nuevo nombre del Intérprete: ")
    apellido = input("Ingrese el nuevo apellido del Intérprete: ")
    nacionalidad = input("Ingrese la nueva nacionalidad del Intérprete: ")
    foto = input("Ingrese la nueva dirección web de la foto del Intérprete: ")
    nuevoInterprete = modelo.Interprete(id_interprete,nombre,apellido,nacionalidad,foto,1)#el 1 es para que no se elimine... mantenerlo vigente
    con = modelo.Conectar()
    con.ModificarInterprete(nuevoInterprete)
    input("Presione ENTER para continuar")

def EliminarInterprete():
    con = modelo.Conectar()
    for i in con.ListarInterprete():
        print(i)
    id_interprete = int(input("\nIngrese el ID del Intérprete que quiere eliminar: "))
    con = modelo.Conectar()
    con.EliminarInterprete(id_interprete)
    input("Presione ENTER para continuar")