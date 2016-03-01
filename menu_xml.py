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

for autor in raiz.findall("autor"):
    print "Grupo:", autor.text

print "Se han encontrado", len(raiz.findall("autor")),"grupos"

#Contar información: Muestra cuantos albunes tiene cada grupo.

dic_autores = {}
for autor in raiz.findall("autor"):
    dic_autores[autor.text] = 0
    if type(autor.getchildren()) == list:
        for album in autor.getchildren():
                dic_autores[autor.text] = dic_autores[autor.text] + 1
    else:
        dic_autores[autor.text] = 1

for grupo in dic_autores.items():
    if grupo[1] >1:
        print "El grupo:", grupo[0][:-9], "posee", grupo[1], "albunes"
    else:
        print "El grupo:", grupo[0][:-9], "posee", grupo[1], "album"

#Buscar o filtrar información: Si se introduce un autor muestra sus albunes, si introduce un album se muestra sus canciones.
print ""
album_autor = raw_input("Introduce un autor o album: ")

for grupo in raiz.findall("autor"):
    if grupo.text.strip() == album_autor:
        for album in grupo.getchildren():
            print "Album:",album.text

for album in raiz.findall("autor/album"):
    if album.text.strip() == album_autor:
        print "El autor del album es: ",album.getparent().text


#Buscar información relacionada: Si se introduce una canción, se muestra el album y su autor.

#Ejercicio libre: Si se introduce un grupo, se muestra toda su discografia y los enlaces a cada uno de sus albunes.


