# Genetic AB Problem
Solución de un problema AB mediante algoritmo genéticos.

Forma parte de los retos compartidos con @okrmartin , @emanzipado y @carlhm y abiertos a cualquier que quiera participar.

## Descripción del problema
El problema no podemos/debemos transcribirlo aquí debido a los derechos de autor de Topcode.com, aunque realmente esto no es lo mas interesante.

Hemos escogido un problema de Topcode.com para solucionarlo mediante un algoritmo genético y, a partir de aquí, desarrollar una librería (en el futuro) para Python donde solo necesitemos introducir la codificación de nuestro cromosoma, definir restricciones y puntuacion y configurar las variables necesarias para poder encontrar el/los mejores individuos de una población.

## Ejecución

Para ejecutarlo necesitaremos tener instalada la versión 2.7 de Python y ejecutar el siguiente comando.

`> python src/run.py [longitud_salida] [pares_encontrados]`

## Salida

La salida que podremos ver por terminal será algo de este estilo 

```
GENERACION : 
[0, 1, 0] Puntuacion 1.0 Pares 1 Total Pares 1
[1, 0, 1] Puntuacion 1.0 Pares 1 Total Pares 1
[0, 0, 1] Puntuacion 2.0 Pares 1 Total Pares 2
[0, 1, 1] Puntuacion 2.0 Pares 1 Total Pares 2
[0, 1, 0] Puntuacion 1.0 Pares 1 Total Pares 1
[0, 1, 0] Puntuacion 1.0 Pares 1 Total Pares 1
[1, 0, 0] Puntuacion 0.0 Pares 1 Total Pares 0
[0, 0, 1] Puntuacion 2.0 Pares 1 Total Pares 2
[0, 0, 0] Puntuacion 0.0 Pares 1 Total Pares 0
[1, 0, 0] Puntuacion 0.0 Pares 1 Total Pares 0
[0, 1, 1] Puntuacion 2.0 Pares 1 Total Pares 2
[1, 0, 1] Puntuacion 1.0 Pares 1 Total Pares 1
[1, 0, 1] Puntuacion 1.0 Pares 1 Total Pares 1
[0, 0, 0] Puntuacion 0.0 Pares 1 Total Pares 0
Solucion 
----------
ABA

```

Lo importante en nuestra salida será la última línea que es la solución real. El resto de texto lo podemos obviar ya que simplemente nos va mostrando los individuos de cada población y su puntuación. 

Una mejora a realizar es imprimir esta salida en un archivo de log 