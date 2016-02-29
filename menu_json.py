#!/usr/bin/python
# coding=utf-8

import json

#Carga de fichero

with open("armas.json") as fichero_json:
    raiz = json.load(fichero_json)

#Listar información: Muestra cuantas armas contiene el juego.

#Contar información: Muestra la clasificación de armas y cuantas pertenecen a cada tipo.

#Buscar o filtrar información: Si se introduce un tipo de armas, se muestran las que pertenecen a esa categoría.

#Buscar información relacionada: Si se introduce el nombre de un arma, se muestra sus especificaciones.

#Ejercicio libre: Muestra el arma que permite al jugador ir más rápido y el arma que más daño resta.