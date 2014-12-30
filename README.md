Qué.Es.Esto: seriesLyks (seriesLeaks)
=========================================

Una copia parcial de los enlaces alojados hasta el 29.12 en series.ly y que fueron retirados por la reforma de la Ley de Propiedad Intelectual.
Motivos del cierre aquí: http://blog.series.ly/2014/12/serieslysigue.html

La copia es parcial porque se ha hecho contrareloj y bajo un proceso de ingeniería inversa y bastante prueba-error hasta que el control de errores para las distintas respuestas del servidor ha quedado mas o menos estabilizado. Teniendo en cuenta que:
+ Durante estos días de navidad el tráfico ha sido intenso.
+ Que probablemente ellos hayan estado toqueteando el servidor de forma intensa en las últimas semanas.
+ Que no he estado todo lo diestro que debía con el código.

Por todo lo anterior y como advertencia -> Mas se perdió en la guerra.

Asi que el aviso queda dejado. Es una copia parcial.


Porqué
======

+ Porque quería conocer la infraestructura de series.ly
+ Porque tenía curiosidad por hacer un proceso de "ingeniería inversa".
+ Porque hacerlo contrarreloj era un reto.
+ Porque la comunidad merecía tomar de vuelta el trabajo aportado a la comunidad


Cuando
======

Por los últimos 10 días.


Cómo
====

Si miras en dev/ verás que con mucho bash scripting, algo de conocimiento http y una pizca de python.
A nivel técnico el proceso era el siguiente:
+ 4 categorías (series, programas de televisión, películas y documentales).
+ X páginas por categoría a unos 50 elementos por página.
+Las cateǵoría de documentales y película no tenían mayor anidación. Series y programas de televisión se anidaban en temporadas y episodios.
+ Para cada episodio (o película o documental) hay que hacer una petición a la api pública de la web, obteniendo una relación de links con cierta información y una id interna.
+ Con la id interna y una llamada a un .php se accedía al link externo (99% de los casos)
+ La información del link de salida estaba contenido en la cabecera location del http de retorno, forzando el servidor a una redirección casi invisible a través de un 302.
+ El resto del código busca prevenir de fallos de servidor (códigos 5xx) debido a las reiteradas caídas del servicio.
+ Por último el ćodigo estaba pensado para tener la capacidad de empezar donde se dejó, aunque debido a las limitaciones del sistema de fichero de Unix, a partir de 80.000 ficheros las salidas eran erróneas y cascaba.


Para qué
========

Desde el desconocimiento de no ser miembro activo de ninguna comunidad de enlaces el instinto me decía que podría haber muchos links interesantes alojados en series.ly que quedarían huérfanos tras la retirada inminente de la visibilidad pública en la web.

De alguna forma, aunque fuese de forma torpe y parcial, la comunidad se merecía obtener una copia de estos links y decidir libremente qué hacer a partir del 1 de Enero, una vez que entre en vigor la mentada ley en España.

No es un repositorio pensado para usuarios, pero si es tu caso y aún así tienes curiosidad, mas adelante puedes encontrar información sobre cómo hacer uso del mismo.


Desarrolladores
===============

Si estás pensando en hacer uso de este repositorio, quizás quieras mirar en los siguientes enlaces:
+ http://www.imdb.com/interfaces
+ http://www.omdbapi.com/

Hay más, pero la idea general es que en todo programa/serie/película/documental hay una id externa a imdb que puede ser utilizada para obtener información más completa y actualizada en otras bases de datos.

Dependiendo de la tecnología que uses, no será muy complicado construir un ORM para volcar todos los ficheros en una bbdd relacional. Yo, personalmente por falta de tiempo, no entra entre mis planes.


Usuarios
========

Si eres usuario de Unix ( MacOs o GNU/Linux ) y no te da miedo la terminal solo necesitas abrir una terminal e introducir:

<code>
	git clone https://github.com/Viperey/seriesLyks
</code>

Si eres usuario de Windows y tienes git instalado en el sistema, no necesitas mucho más.
Si eres usuario de Mac o Windows y tienes conocimientos limitados en materia, puedes instalar un cliente para hacer una copia del repositorio y a partir de ahí ver la base de datos directamente en tu ordenador.

Para ello puedes usar SourceTree: http://www.sourcetreeapp.com/ y seguir el siguiente link: https://answers.atlassian.com/questions/58249/how-to-clone-in-sourcetree


Legal
=====

1. No hay un objetivo de lucro en todo este proceso. Lo he hecho porque la comunidad merece recuperar estos contenidos y decidir sobre el futuro de los mismos.
2. Este proceso no ha sido llevado a cabo desde España, ni físicamente ni las infraestructuras de soporte que se han utilizado.


Disclaimers varios
==================

1. La ley que entra en vigor que ha forzado a cerrar la web de la que parte este contenido (y muchas otras) está haciendo un severo daño a las comunidades de intercambios de enlaces, que al igual que en tiempos pasados y anteriores leyes, sabrá encontrar el camino para volver a resurgir.

2. Personalmente, considero que la cultura debe ser accesible para todos, que la industria de los contenidos debe adaptarse a un tiempo en que los usuarios tienen el poder.

3. En los próximos tiempos estas industrias van a perder muchísimos privilegios y poder (si no lo han hecho ya), las leyes que imponen son una muestra de como defienden con todas las armas posibles sus privilegios. Las detenciones y acoso a los fundadores de TPB, las leyes que se han creado a lo largo y ancho de Europa son sólo minúsculas muestras de ello. Las comunidades sabrán encontrar el camino para que el campo siga sin puertas.

4. Aunque se puede poner puertas al campo, si alguien está dipuesto a gastar semejante cantidad de energía en cargarse el campo en vez de contribuir al mismo, no merece respeto ni temor alguno por las leyes que consigan imponer a los distintos gobiernos. La desobediencia a industria y gobierno en cuestiones de contenidos culturales se ve como una obligación a la luz de los hechos acontecidos en los últimos tiempos. 

5. Personalmente, no comparto que las webs de enlaces busquen el lucro empresarial o personal con sus actividades. La cultura debe ser accesible y el intercambio de enlaces debería ser una forma de crear nuevas formas de cultura y comunidad. Las webs que persiguen beneficios a costa del trabajo ajeno hacen un flaco favor a las causas y las ventanas de oportunidad que la nueva era tecnológica abren. No deseo mantener el control sobre el devenir de estos datos, básicamente porque es imposible, pero si pudiese elegir, preferiría que fuesen utilizadas para seguir aportando y mejorando la red, no para convertirla en un espacio aún más mercantilizado y entregado a las empresas y el dinero.

6. Por último, al igual que hice yo, haced lo que os salga del pie.
