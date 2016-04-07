# ApuestasDeportivas

##Introducción a la aplicación

Para el inico de la aplicación deberás iniciar sesión con los siguientes datos:

* User: diego
* Password: abal

Una nueva aplicación de apuestas deportivas sale a la luz, en este caso, será una base de datos propia del usuario para almacenar 
sus partidos, en ella podrá guardar el código(1235), evento(Celta-Depor), pronóstico(1X2) y cuota (@2.10). Todos los datos serán
guardados en una base de datos llamada apuestas.

La aplicación cuenta con excepciones, epydoc, ventanas emergentes y reportlab, esto último generará un documento PDF con el contenido de la base de datos.

##Métodos utilizados:

* Inserción: El usuario deberá introducir cuatro campos (código, evento, pronóstico y cuota), cada campo tiene una longitud máxima, 
y un contenido específico, es decir, en caso de que el usuario introduzca mal los datos, saldrá una ventana emergente diciendo el 
error que esta sucediendo, lo más probable es datos invalidos.

* Modificar: Permite modificar un registro mediante el código, el usuario debe poner el código que quiere modificar, y debajo los 
datos que quiere cambiar, cuando el usuario clickée en modificar, saldra una ventana emergente diciendo registro modificado, si no, 
datos invalidos.

* Borrar: Este método permite borrar los registros mediante el código, en el momento que el usuario clickée en borrar, se borrará 
automaticamente de la base de datos.

* Consultar: Por último, este método permitirá sacar todo el contenido de la base de datos.

Diego Abal Rodríguez


