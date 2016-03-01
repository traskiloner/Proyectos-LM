#!/usr/bin/python
# coding=utf-8

import json

#Carga de fichero

with open("armas.json") as fichero_json:
    raiz = json.load(fichero_json)

#Listar información: Muestra cuantas armas contiene el juego.

print "El juego contiene:", len(raiz["weapons"]), "armas"

#Contar información: Muestra la clasificación de armas y cuantas pertenecen a cada tipo.

dic_armas = {}
for arma in raiz["weapons"]:
    if arma["type"] in dic_armas.keys():
        dic_armas[arma["type"]] = dic_armas[arma["type"]] + 1
    else:
        dic_armas[arma["type"]] = 1

for tipo in dic_armas.items():
    print "El tipo", tipo[0],"contiene", tipo[1],"armas"

#Buscar o filtrar información: Si se introduce un tipo de armas, se muestran las que pertenecen a esa categoría.
print ""
print "Recuerda que los tipos de armas son los siguientes:"

lista_tipos = []
for tipo in raiz["weapons"]:
    if tipo["type"] not in lista_tipos:
        lista_tipos.append(tipo["type"])
        print tipo["type"]

print ""
tipo_arma = raw_input("Introduce el tipo de arma: ")

for arma in raiz["weapons"]:
    if arma["type"].lower() == tipo_arma.lower():
        print ""
        print "Arma:", arma["name"]
        print "Precio:", arma["price"]
        print "Daño:", arma["damage"]

#Buscar información relacionada: Si se introduce el nombre de un arma, se muestra sus especificaciones.

#Ejercicio libre: Muestra el arma que permite al jugador ir más rápido y el arma que más daño resta.