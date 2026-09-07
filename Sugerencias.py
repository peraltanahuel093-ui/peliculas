print("========================\n")
print("Sugerencias de Peliculas\n")
print("========================\n")
usuario=input("Buen dia, cual es tu nombre? ")
print("¿Que queres ver hoy,"+usuario+"?")
nombre_pelicula="Rapido y furioso"
genero_pelicula="Accion"
anio_pelicula=2001
rating_pelicula=6.8
nombre_pelicula2="Troya"
genero_pelicula2="Accion"
anio_pelicula2=2004
rating_pelicula2=7.4
nombre_pelicula3="El Transportador"
genero_pelicula3="Accion"
anio_pelicula3=2002
rating_pelicula3=6.8
nombre_pelicula4="Y donde esta el piloto?"
genero_pelicula4="Comedia"  
anio_pelicula4=1980 
rating_pelicula4=7.7 
nombre_pelicula5="American Pie"
genero_pelicula5="Comedia"
anio_pelicula5=1999
rating_pelicula5=7.0
nombre_pelicula6="Tiempos Modernos"
genero_pelicula6="Comedia"
rating_pelicula6=8.5
anio_pelicula6=1936
print("---- GÉNEROS-----")
print("Acción")
print("Comedia")
genero_favorito=input("¿Que genero te gusta? ")
print ("Buscando Péliculas del Género: " +genero_favorito)
if (genero_pelicula==genero_favorito):
	print(nombre_pelicula)
if (genero_pelicula2==genero_favorito):
    print(nombre_pelicula2)
if (genero_pelicula3==genero_favorito):
    print(nombre_pelicula3)
if (genero_pelicula4==genero_favorito):
    print(nombre_pelicula4)
if (genero_pelicula5==genero_favorito):
    print(nombre_pelicula5) 
if (genero_pelicula6==genero_favorito):
    print(nombre_pelicula6) 