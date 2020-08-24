"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from Sorting import insertionsort as sor1
from Sorting import selectionsort as sor2
from Sorting import shellsort as sor3
from DataStructures import linkedlistiterator as il
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from DataStructures import singlelinkedlist as ls

from time import process_time 


def loadCSVFile (file, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print('5- Crear ranking de peliculas')
    print('6- Conocer a un director')
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria,l1,l2,id):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    t1_start = process_time() #tiempo inicial
    #creo una lista para guardar id de peliculas por director
    l_movies= lt.newList()

    for i in l1['elements']:
        if i['director_name'] == criteria:
            l_movies['elements'].append(i['id'])
    l_movies['size'] = len(l_movies['elements'])
    print(l_movies['elements'])
    counter = 0
    data = lt.newList()
    data['average'] = 0.0

    for i in range(len(l2['elements'])-1):
        if l2['elements'][i][id] == l_movies['elements'][counter]:
            if counter < len(l_movies['elements']) - 1:
                data['elements'].append(l2['elements'][i]["original_title"])
                data['average'] += (float(l2['elements'][i]['vote_average']))
                counter += 1
                

    data['size'] = len(data['elements'])
    pr = data['average']/(len(data))
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos") 
    return (data['elements'],data['size'],pr)

def orderElementsByCriteria(function,lst):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    t1_start = process_time() #tiempo inicial

    lst_count = lt.newList()
    lst_count['elements'] = [[],{}]
    print(lst_count)
    
    lst_average = lt.newList()
    lst_average['elements'] = [[],{}]

    for i in range(lt.size(lst)):
        lst_count['elements'][0].append(int(lst['elements'][i]['vote_count']))
        lst_count['elements'][1][lst['elements'][i]['vote_count']] = lst['elements'][i]['original_title']
        lst_average['elements'][0].append(float(lst['elements'][i]['vote_average']))
        lst_average['elements'][1][lst['elements'][i]['vote_average']] = lst['elements'][i]['original_title']
    
    if function == '1':
        lst_count['elements'][0] = sor1.insertionSort(lst_count['elements'][0])
        lst_average['elements'][0] = sor1.insertionSort(lst_average['elements'][0])
    elif function == '2':
        lst_count['elements'][0] = sor2.selectionSort(lst_count['elements'][0])
        lst_average['elements'][0] = sor2.selectionSort(lst_average['elements'][0])
    elif function == '3':
        lst_count['elements'][0] = sor3.shellSort(lst_count['elements'][0])
        lst_average['elements'][0] = sor3.shellSort(lst_average['elements'][0])
    
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return (lst_count,lst_average)

def menuReq2():
    print("1. Ordenamiento por insertion sort")
    print("2. Ordenamiento por selection sort")
    print("3. Ordenamiento por shell sort")

def opcionesReq2():
    menuReq2()
    opcion = input("Seleccione el tipo de ordenamiento: ")
    continuar = True
    while continuar == True:
        if opcion == '1':
            continuar = False
            ans = opcion
        elif opcion == '2':
            continuar = False
            ans = opcion
        elif opcion == '3':
            continuar = False
            ans = opcion
        else:
            print("Elija una opcion correcta")
            menuReq2()
            opcion = input("Digite su respuesta: ")
    return ans

def menuReq1():
    print('1. Probar con archivos grandes')
    print('2. Probar con archivos pequeños')
    opcion = input('Digite su opcion: ')
    return opcion

def opcionesReq():
    opcion = menuReq1()
    continuar = True
    while continuar == True:
        if opcion == '1':
            direc1 = 'Data/theMoviesdb/AllMoviesCastingRaw.csv'
            direc2 = 'Data/theMoviesdb/AllMoviesDetailsCleaned.csv'
            id = '\ufeffid'
            continuar = False 
        elif opcion == '2':
            direc1 = 'Data/theMoviesdb/MoviesCastingRaw-small.csv'
            direc2 = 'Data/theMoviesdb/SmallMoviesDetailsCleaned.csv'
            id = 'id'
            continuar = False
        else:
            opcion = input('Opcion errada, digite nuevamente su opcion: ')
    return (direc1, direc2,id)


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = lt.newList()   # se require usar lista definida
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                lista = loadCSVFile("Data/test.csv") #llamar funcion cargar datos
                print("Datos cargados, ",lista['size']," elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene ",lista['size']," elementos")
            elif int(inputs[0])==3: #opcion 3
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsFilteredByColumn(criteria, "nombre", lista) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsByCriteria(criteria,0,lista)
                    print("Coinciden ",counter," elementos con el crtierio: '", criteria ,"' (en construcción ...)")
            elif int(inputs[0])==5:
                lst = loadCSVFile(opcionesReq()[1])
                data = orderElementsByCriteria(opcionesReq2(),lst)
                print('Lista de los 10 más votados: ')
                counter = 0
                for i in data[0]['elements'][0]:
                    if counter == 11:
                        break
                    print(counter+'- '+data[0]['elements'][1][i])
                print('Lista de los 10 mejores promedios: ')   
                counter = 0
                for i in data[1]['elements'][0]:
                    if counter == 11:
                        break
                    print(counter+'- '+data[1]['elements'][0][i])
            elif int(inputs[0])==6:
                opciones = opcionesReq()
                lst1 = loadCSVFile(opciones[0])
                lst2 = loadCSVFile(opciones[1])
                director = input('Digite el director: ')
                data = countElementsByCriteria(director,lst1,lst2,opciones[2])
                print('El director ', director,' ha dirigido ',data[1],' peliculas')
                print('El promedio de las peliculas del director',director,' es ',data[2])
                print('Las peliculas que ha dirigido son: ')
                x = 1
                for i in data[0]:
                    print(i,x)
                    x += 1
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()