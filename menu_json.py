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
print ""

print "Recuerda que las armas son las siguientes:"
for arma in raiz["weapons"]:
    print arma["name"]

print ""
nombre_arma = raw_input("Introduce el nombre del arma: ")
for arma in raiz["weapons"]:
    if arma["name"].lower() == nombre_arma.lower():
        print "Nombre:", arma["name"]
        print "Tipo:", arma["type"]
        print "Precio:", arma["price"]
        print "Daño:", arma["damage"]
        print "Tamaño del cargador:", arma["clip_size"]
        print "Retroceso:", arma["recoil_magnitude"]


#Ejercicio libre: Muestra el arma que permite al jugador ir más rápido y el arma que más daño resta.
print ""
dic_libre = {"nombre_damage":"","valor_damage":0,"nombre_rapida":"","valor_rapida":0,"nombre_relacion":"","valor_relacion":0}

for arma in raiz["weapons"]:
    if arma["damage"] >= dic_libre["valor_damage"]:
        dic_libre["valor_damage"] = arma["damage"]
        dic_libre["nombre_damage"] = arma["name"]

    if arma["max_player_speed"] >= dic_libre["valor_rapida"]:
        dic_libre["valor_rapida"] = arma["max_player_speed"]
        dic_libre["nombre_rapida"] = arma["name"]

    if (arma["max_player_speed"] / arma["damage"]) >= dic_libre["valor_relacion"]:
        dic_libre["valor_relacion"] = (arma["max_player_speed"] / arma["damage"])
        dic_libre["nombre_relacion"] = arma["name"]

print "El arma más rapida es:", dic_libre["nombre_rapida"]
print "El arma que realiza más daño es: ", dic_libre["nombre_damage"]
print "El arma con la relación velocidad/daño más alta es:", dic_libre["nombre_relacion"]

#Ejercicio añadido: genera fichero html
fichero_html = open("armas.html","w")

for arma in raiz["weapons"]:
    nombre_arma = '<h1>' + arma["name"] + '</h1>'
    fichero_html.write(nombre_arma)

    tipo_arma = '<p>' + arma["type"] + '</p>'
    fichero_html.write(tipo_arma)

    modelo_arma = '<a href="' + arma["model_world"] + '">Modelo</a>'
    fichero_html.write(modelo_arma)