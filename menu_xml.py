#!/usr/bin/python
# coding=utf-8

from lxml import etree

#Carga del fichero XML
def carga_xml():
    try:
        xml_completo = etree.parse("musica_utf8.xml")
    except:
        return "error"
if carga_xml() == "error":
    "Debe existir el fichero musica_utf8.xml en el directorio"
else:
    xml_completo = etree.parse("musica_utf8.xml")
    raiz = xml_completo.getroot()

#Listar información: Muestra los diferentes Autores/Grupos que contiene.
print "En el fichero se encuentran los siguientes grupos: "
lista_autores = raiz.findall("autor")
for autor in lista_autores:
    print "Grupo:", autor.text

print "Se han encontrado", len(lista_autores),"grupos"
#Contar información: Muestra cuantos albunes tiene cada grupo.

#Buscar o filtrar información: Si se introduce un autor muestra sus albunes, si introduce un album se muestra sus canciones.

#Buscar información relacionada: Si se introduce una canción, se muestra el album y su autor.

#Ejercicio libre: Si se introduce un grupo, se muestra toda su discografia y los enlaces a cada uno de sus albunes.


