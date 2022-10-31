#LISTA DE MUSICAS

ListaArtistas = [["1-Tini"], ["2-Soledad Pastorutti"], ["3-Axel"], ["4-Karon G"], ["5-Manuel Turizo"]]
ListaCanciones = [["Ultimo beso"], ["Tal como siento"], ["Somos lo que fuimos"], ["Gatubela"], ["La bachata"]]
ListaLetras = [["1-Y ahora que no estás tú, Soy fría, como un iglú, Estoy llamando a todo' lo' que no les di Como hiciste con mi cora, a todo' los partí"], ["2-Vamos a volar un rato,Se me ocurren tantas cosas, Hoy la calma es tan hermosa,Que se me olvida el reproche, Desnudemos una noche, Esta vida silenciosa"],["3-Recuerdo aquellos tiempos de largas esperas y esperanzas,Donde el abrazo nos partía los huesos y nos arreglaban, Éramos tú y yo cuidándonos la espalda, Proyectando sueños, pensado en mañana"], ["4-'Taba loca por probarte,Darte lo' besito' yo,Ojalá pueda' quedarte, Porque así me quedo yo"], ["5-Ando manejando,Por las calles que me besaste,Oyendo las canciones, Que un día me dedicaste"]]

def elecciones():
    while True:
        try: 
             eleccion = int(input("Que te gustaria saber?\n 0- Finalizar\n 1- Ver lista de artistas \n 2- Ver lista de canciones \n 3- Ver la letra de las caciones \n 4- Agregar cancion \n 5- Volver a las preguntas \n 6- buscar por nombre \n : "))
            
             if eleccion == 1:
                verartistas()
             if eleccion == 2:
               vercanciones()
             if eleccion == 3:
              seleccionarletra()
             if eleccion == 4:
              agregarcancion()
             if eleccion == 5:
                elecciones()
             if eleccion == 6:
                buscarnombre()
             else:
               if eleccion == 0:
                print ("Muchas gracias")
                break


        except:
          print("Error en la eleccion\n elegir una opcion Numerica:")
          eleccion = int(input("1-intentar de nuevo? \n2- Cerrar programa \n:"))
          if eleccion == 1:
            elecciones()
          if eleccion == 2:
            print("El programa finalizo")

#Funcion para ver la lista de los artistas

def verartistas():
    print("Estas son los artistas \n")
    for i in ListaArtistas:
        print(i) 
    elecciones()

def vercanciones():
    print ("Estas son las canciones  \n")
    for i in ListaCanciones:
        print(i)
    elecciones()

def verletras():
    print("Estas es la letra  \n")
    for i in ListaLetras:
        print(i)
    elecciones()

#Funcion para seleccionar la cancion

def seleccionarcancion():
    cancion = int(input("que cancion quieres escuchar?: "))
    print(ListaCanciones[cancion-1])

#funcion para seleccionar la letra

def seleccionarletra():
    letra = int(input("que letra quieres leer?: "))
    print(ListaLetras[letra-1])

#Funcion para agregar una cancion

def agregarcancion():
    eleccion = input("Agregar nombre del artista: ")
    eleccion2 = input ("agregar nombre de canciones")
    eleccion3 = ingresarletra()
    ListaArtistas.append(eleccion)
    ListaCanciones.append(eleccion2)
    print("Cancion Agregada")
    elecciones()

#buscar por Nombre

def buscarnombre():
    texto = str(input("Ingrese el nombre de la cancion "))
    for i in ListaCanciones:
        if (texto in i[0]):
         print("\n Su cancion es la numero", ListaCanciones.index(i)+1 , "-", i[0])

#Funcion para ingresar letra

def ingresarletra():
    eleccion = ""
    print("Ingrese la letra de la canción. Para nuevo renglón enter y la letra W para terminar")
    letra = input()
    while eleccion == "w" and eleccion == "W":
        eleccion = eleccion + "\n" + letra
        eleccion = input("Ingrese nueva línea, w para terminar\n")
        ListaLetras.append(letra)
    return eleccion

elecciones()
