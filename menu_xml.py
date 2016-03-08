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
    print "Debe existir el fichero musica_utf8.xml en el directorio"

else:
    xml_completo = etree.parse("musica_utf8.xml")
    raiz = xml_completo.getroot()
    print "Introduce 1 para mostrar los grupos que contiene el fichero XML"
    print "Introduce 2 para contar los albunes que tiene cada grupo"
    print "Introduce 3 para buscar los albunes de un grupo o sus canciones"
    print "Introduce 4 para buscar información sobre una canción"
    print "Introduce 5 para obtener las URLs de la discografia de un grupo"
    print "Introduce 6 para generar un fichero HTML"
    opcion = raw_input("Opción: ")


    if opcion in locals().values() and opcion == "1":

    #Listar información: Muestra los diferentes Autores/Grupos que contiene.

        print "En el fichero se encuentran los siguientes grupos: "

        for autor in raiz.findall("autor"):
            print "Grupo:", autor.text

        print "Se han encontrado", len(raiz.findall("autor")),"grupos" , len(raiz.findall("autor/album")),"albunes y", len(raiz.findall("autor/album/cancion")), "canciones"

    if opcion in locals().values() and opcion == "2":

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

    if opcion in locals().values() and opcion == "3":

        #Buscar o filtrar información: Si se introduce un autor muestra sus albunes, si introduce un album se muestra sus canciones.
        print ""
        album_autor = raw_input("Introduce un autor o album: ")
        encontrado = False

        for grupo in raiz.findall("autor"):
            if grupo.text.strip().lower() == album_autor.lower() and encontrado is False:
                for album in grupo.getchildren():
                    print "Album:",album.text
                    encontrado = True

        if encontrado is True:
            for album in raiz.findall("autor/album"):
                if album.text.strip().lower() == album_autor.lower():
                    print "El autor del album es: ",album.getparent().text
                    encontrado = True
        else:
            print "No se ha encontrado album o autor"

    if opcion in locals().values() and opcion == "4":

        #Buscar información relacionada: Si se introduce una canción, se muestra el album y su autor.
        print ""

        nombre_cancion = raw_input("Introduce el nombre de una cancion: ")
        encontrado = False

        for cancion in raiz.findall("autor/album/cancion"):
            if cancion.text.lower() == nombre_cancion.lower() and encontrado is False:
                print "Cancion encontrada:", cancion.text
                print "Album:", cancion.getparent().text
                print "Autor:", cancion.getparent().getparent().text
                encontrado = True

        if encontrado is False:
            print "Canción no encontrada"

    if opcion in locals().values() and opcion == "5":

        #Ejercicio libre: Si se introduce un grupo, se muestra toda su discografia y los enlaces a cada uno de sus albunes.
        print ""

        nombre_grupo = raw_input("Introduce un grupo: ")
        encontrado = False
        for autor in raiz.findall("autor"):
            if autor.text.strip().lower() == nombre_grupo.lower() and encontrado is False:
                print "Grupo:", autor.text
                for album in autor.getchildren():
                    print "Album:", album.text.strip()
                    for url in album.getchildren():
                        if url.text.startswith("http"):
                            print "URL", url.text
                            print ""
                encontrado = True

        if encontrado is False:
            print "No se ha encontrado el grupo"

    if opcion in locals().values() and opcion == "6":
        anyo = raw_input("Introduce un año: ")
        encontrado = False
        fichero_html = open('musica.html',"w")
        for album in raiz.findall("autor/album"):
            if album.attrib.values()[0] == anyo:

                autor = "<h1>" + album.getparent().text[:-9] + "</h1>"
                disco = "<p>" + album.text[:-13] + "</p>"
                imagen = '<img src="' + album.find("url_imagen").text + '" width=20%>'
                url_torrent = '<a href="' + album.find("url_torrent").text + '">' + 'Descargar torrent</a>'

                encontrado = True

                fichero_html.write(imagen)
                fichero_html.write(autor)
                fichero_html.write(disco)
                fichero_html.write(url_torrent)
                fichero_html.write('</br>')
                fichero_html.write('\n')

        if encontrado is False:
            print "No se ha encontrado ningún album en", anyo
