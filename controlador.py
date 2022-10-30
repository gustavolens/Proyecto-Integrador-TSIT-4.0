import modelo
# Módulos Rich:
from rich.table import Table
from rich.console import Console
from rich.align import Align
from rich import box

console = Console(width=100)

# Listar artistas, género, discográfica y formato
#---------------------------------------------------------------------------------------
def ListarArtistasVigentes():
    con = modelo.Conectar()
    table = Table(title="Estos son los intérpretes vigentes actualmente:")
    columnas = ["ID", "APELLIDO", "NOMBRE", "NACIONALIDAD", "URL FOTO"]
    for col in columnas:
        table.add_column(col, style="cyan", justify="center")
    
    for i in con.ListarInterprete():
        table.add_row(str(i[0]), str(i[2]), str(i[1]), str(i[3]), str(i[4]))

    console.print(Align.center(table))

def ListarGenero():
    con = modelo.Conectar()
    table = Table(title="Géneros:")
    columnas = ["ID", "NOMBRE"]
    for col in columnas:
        table.add_column(col, style="cyan", justify="center")
    
    for i in con.ListarGenero():
        table.add_row(str(i[0]), str(i[1]))

    console.print(Align.center(table))

def ListarDiscografica():
    con = modelo.Conectar()
    table = Table(title="Discográfica:")
    columnas = ["ID", "NOMBRE"]
    for col in columnas:
        table.add_column(col, style="cyan", justify="center")
    
    for i in con.ListarDiscografica():
        table.add_row(str(i[0]), str(i[1]))

    console.print(Align.center(table))

def ListarFormato():
    con = modelo.Conectar()
    table = Table(title="Formato:")
    columnas = ["ID", "TIPO"]
    for col in columnas:
        table.add_column(col, style="cyan", justify="center")
    
    for i in con.ListarFormato():
        table.add_row(str(i[0]), str(i[1]))

    console.print(Align.center(table))

# Listar álbums
#---------------------------------------------------------------------------------------
def ListarAlbumesPorArtistas():
    con = modelo.Conectar()
    listado = con.ListarAlbumes()
    
    table = Table(title="Álbumes por Artistas")
    columnas = ["APELLIDO", "NOMBRE", "COD. ÁLBUM", "ÁLBUM", "GÉNERO", "DISCOGRÁFICA", "PRECIO", "CANTIDAD", "FORMATO"]
    for col in columnas:
        table.add_column(col, style="cyan", justify="center")
    
    for album in listado:
        table.add_row(str(album[0]), str(album[1]), str(album[2]), str(album[3]), str(album[4]), str(album[5]), str(album[6]), str(album[7]), str(album[8]))
    console = Console()
    console.print(table)

def ListarAlbumesPorGenero():
    con = modelo.Conectar() 
    listado = con.ListarPorGenero()
    
    table = Table(title="Álbumes por Género")
    columnas = ["GÉNERO", "COD. ÁLBUM", "ÁLBUM", "APELLIDO ARTISTA", "NOMBRE ARTISTA", "DISCOGRÁFICA", "PRECIO", "CANTIDAD", "FORMATO"]
    for col in columnas:
        table.add_column(col, style="light_sea_green", justify="center")
    
    for album in listado:
        table.add_row(str(album[0]), str(album[1]), str(album[2]), str(album[3]), str(album[4]), str(album[5]), str(album[6]), str(album[7]), str(album[8]))
    console = Console()
    console.print(table)    

def ListarBusquedaNombreAlbum():
    con = modelo.Conectar()

    tabla_busqueda = Table(expand=True, style="cyan", box=box.ASCII2, show_header=False)
    tabla_busqueda.add_row("[i]Ingrese el [bold cyan]nombre del álbum[/][/i] que desea buscar: ")
    console.print(tabla_busqueda)

    # Asegurar que ingrese un valor. 
    nombre = ""
    while nombre == "":
        nombre = console.input("[bold cyan]>: ")
        if nombre == "":
            console.rule("", style="bold red1")
            console.print("[i]Por favor, ingrese [bold cyan]nombre del álbum[/][/i]: ")
        

    table = Table(title="Albumes coincidentes: ")
    coincidencias = con.ListarBusquedaNombreAlbum(nombre)
    table.add_column("ID", style="cyan",justify="center")
    table.add_column("COD. ÁLBUM", style="cyan", justify="center")
    table.add_column("NOMBRE", style="cyan", justify="center")
    table.add_column("ID INTÉR.", style="cyan", justify="center")
    table.add_column("ID GÉN.", style="cyan", justify="center")
    table.add_column("CANT. TEMAS", style="cyan", justify="center")
    table.add_column("ID DISCO.", style="cyan", justify="center")
    table.add_column("ID FORMATO", style="cyan", justify="center")
    table.add_column("FECHA", style="cyan", justify="center")
    table.add_column("PRECIO", style="cyan", justify="center")
    table.add_column("CANTIDAD", style="cyan", justify="center")
    
    if len(coincidencias) == 0:
        console.print("[i][bold red1]No[/] se encontraron coincidencias[/i]. :x:", justify="center")
        return

    for album in coincidencias:
        table.add_row(str(album[0]), str(album[1]), str(album[2]), str(album[3]), str(album[4]), str(album[5]), str(album[6]), str(album[7]), str(album[8]), str(album[9]), str(album[10]))
    
    console.print(table)
    return

# ABM álbums
#---------------------------------------------------------------------------------------
def InsertarAlbum():
    console.rule("", style="bold orange_red1")
    cod_album = int(console.input("[i]Ingrese el [cyan bold]código[/] del nuevo álbum[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    nombre = console.input("[i]Ingrese el [cyan bold]nombre[/] del álbum[/i][bold cyan]: ")
    console.rule("", style="bold orange_red1")

    # Hay que tener los siguientes datos ya dentro de la base:
    con = modelo.Conectar()

    ListarArtistasVigentes()

    console.rule("", style="bold orange_red1")
    console.print("[i]En caso de que el Intérprete [bold red1]no[/] esté en la lista, [bold cyan]ingrese 0[/] para agregarlo.[/i]")  
    id_interprete = int(console.input("[i]Ingrese el [bold cyan]ID[/] del intérprete[/i][bold cyan]: "))
    id_interprete = InsertarInterprete() if id_interprete == 0 else id_interprete # Hago una Operación Ternaria para que el ListarGenero() sí se ejecute.
    console.rule("", style="bold orange_red1")

    ListarGenero()
    console.rule("", style="bold orange_red1")
    id_genero = int(console.input("[i]Ingrese el [bold cyan]ID[/] del Género[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    cant_temas = int(console.input("[i]Ingrese la [bold cyan]cantidad[/] de temas[/i][bold cyan]: ")) # Menos este, por supuesto.
    console.rule("", style="bold orange_red1")

    ListarDiscografica()
    console.rule("", style="bold orange_red1")
    id_discografica = int(console.input("[i]Ingrese el [bold cyan]ID[/] de la discografica[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")

    ListarFormato()
    console.rule("", style="bold orange_red1")
    id_formato = int(console.input("[i]Ingrese el [bold cyan]ID[/] del formato[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    # Hasta acá.
    fec_lanzamiento = console.input("[i]Ingrese la [bold cyan]fecha de lanzamiento[/] (aaaa-mm-dd)[bold cyan]: ")
    console.rule("", style="bold orange_red1")
    precio = float(console.input("[i]Ingrese el [bold cyan]precio[/][/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    cantidad = int(console.input("[i]Ingrese [bold cyan]cantidad disponible[/] de este álbum[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    caratula = console.input("[i]Ingrese la [bold cyan]dirección web[/] de la Carátula[/i][bold cyan]: ")
    console.rule("", style="bold orange_red1")

    nuevoAlbum = modelo.Album(0,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula,1)
    con.InsertarAlbum(nuevoAlbum)
    # Cod Hernán (idea de mostrar albums despues de insertar):
    #listadoA = con.ListarAlbumes()
    #for album in listadoA:
    #    print(album)

def ModificarAlbum():
    ListarAlbumesPorArtistas()

    console.rule("", style="bold orange_red1")
    cod_album = int(console.input("[i]Ingrese el código del [bold cyan]Álbum[/] que quiere modificar[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    nombre = console.input("[i]Ingrese el [bold cyan]nuevo nombre[/] del álbum[/i][bold cyan]: ")
    console.rule("", style="bold orange_red1")

    # Hay que tener los siguientes datos ya dentro de la base:
    con = modelo.Conectar()

    ListarArtistasVigentes()
    console.rule("", style="bold orange_red1")
    id_interprete = int(console.input("[i]Ingrese el [bold cyan]ID[/] del intérprete[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")

    ListarGenero()
    console.rule("", style="bold orange_red1")
    id_genero = int(console.input("[i]Ingrese el [bold cyan]ID[/] del Género[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    cant_temas = int(console.input("[i]Ingrese la [bold cyan]cantidad[/] de temas[/i][bold cyan]: ")) # Menos este, por supuesto.
    console.rule("", style="bold orange_red1")


    #cant_temas = int(input("\nIngrese la cantidad de temas: ")) # Menos este, por supuesto.
    ListarDiscografica()
    console.rule("", style="bold orange_red1")
    id_discografica = int(console.input("[i]Ingrese el [bold cyan]ID[/] de la discografica[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    

    ListarFormato()
    console.rule("", style="bold orange_red1")
    id_formato = int(console.input("[i]Ingrese el [bold cyan]ID[/] del formato[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    # Hasta acá.
    fec_lanzamiento = console.input("[i]Ingrese la [bold cyan]fecha de lanzamiento[/] (aaaa-mm-dd)[bold cyan]: ")
    console.rule("", style="bold orange_red1")
    precio = float(console.input("[i]Ingrese el [bold cyan]precio[/][/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    cantidad = int(console.input("[i]Ingrese [bold cyan]cantidad disponible[/] de este álbum[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    caratula = console.input("[i]Ingrese la [bold cyan]dirección web[/] de la Carátula[/i][bold cyan]: ")
    console.rule("", style="bold orange_red1")

    nuevoAlbum = modelo.Album(0,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula,1)
    con.ModificarAlbum(nuevoAlbum)
    # Cod Hernán (idea de mostrar albums despues de insertar):
    #listadoA = con.ListarAlbumes()
    #    for album in listadoA:
    #        print(album)
def EliminarAlbum():
    ListarAlbumesPorArtistas()
    
    console.rule("", style="bold orange_red1")
    cod_album = int(console.input("[i]Ingrese el [bold cyan]código del Álbum[/] que quiere eliminar[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")

    # Cod Hernán (idea de mostrar albums despues de insertar):
    #listadoA = con.ListarAlbumes()
    #    for album in listadoA:
    #        print(album)
    con = modelo.Conectar()
    con.EliminarAlbum(cod_album)

# ABM intérpretes
#---------------------------------------------------------------------------------------
def InsertarInterprete():
    datos = ["el [cyan bold]nombre[/]", "el [cyan bold]apellido[/]", "la [cyan bold]nacionalidad[/]", "la [cyan bold]foto[/]"] 
    inputs = []
    for i in datos:
        console.rule("", style="bold orange_red1")
        inputs.append(console.input("[i]Ingrese "+ i +" del intérprete[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    
    nuevoInterprete = modelo.Interprete(0, inputs[0], inputs[1], inputs[2], inputs[3], 1)#El 1 es para darlo de alta en vigente. Si el vigente es 0 (false) no se mostrará.
    con = modelo.Conectar()
    return con.InsertarInterprete(nuevoInterprete) 

def ModificarInterprete():
    ListarArtistasVigentes()
    datos = ["el [cyan bold]ID[/]", "el [cyan bold]nuevo nombre[/]", "el [cyan bold]nuevo apellido[/]", "la [cyan bold]nueva nacionalidad[/]", "la [cyan bold]nueva dirección web[/] de la foto"]
    inputs = []
    for i in datos:
        console.rule("", style="bold orange_red1")
        if i == "el [cyan bold]ID[/]":
            inputs.append(console.input("[i]Ingrese "+ i +" del intérprete que quiere modificar[/i][bold cyan]: "))
            continue
        inputs.append(console.input("[i]Ingrese "+ i +" del intérprete[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    
    nuevoInterprete = modelo.Interprete(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], 1)#el 1 es para que no se elimine... mantenerlo vigente
    con = modelo.Conectar()
    con.ModificarInterprete(nuevoInterprete)

def EliminarInterprete():
    ListarArtistasVigentes()
    console.rule("", style="bold orange_red1")
    id_interprete = int(console.input("[i]Ingrese el [bold cyan]ID[/] del intérprete que quiere eliminar[/i][bold cyan]: "))
    console.rule("", style="bold orange_red1")
    
    con = modelo.Conectar()
    con.EliminarInterprete(id_interprete)