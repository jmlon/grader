# Tipos de datos abstractos y Estructuras básicas

En está práctica se implementará el ADT Conjunto utilizando listas enlazadas (LinkedList) y se implementan algunas de las principales operaciones de conjuntos.
Las principales características a tener en cuenta en la implementación del conjunto es que no se permiten elementos repetidos y que el orden de los elementos en el conjunto no es importante.

## API del ADT  Conjunto

|Operación|Descripción|
|:---|:---|
|Conjunto(T[] elementos)|Constructor a partir de un arreglo de elementos de tipo genérico T.|
|Conjunto union(Conjunto b)|Retorna el conjunto unión: A∪B|
|Conjunto intersección(Conjunto b)|Retorna el conjunto intersección: A∩B|
|Conjunto diferencia(Conjunto b)|Retorna el conjunto diferencia: A-B|
|Conjunto diferenciaSimétrica(Conjunto b)|Retorna la diferencia simétrica (los elementos que están en A o en B, pero no en ambos): A△B|
|boolean equals(Object obj)|Igualdad de conjuntos|
|String toString()|Representación textual, e.g. {a,b,c}|

## Ejercicios a desarrollar

1. Dar una implementación del ADT Conjunto basado en el uso de una lista simplemente enlazada para representar el conjunto. Implementar las operaciones del API previamente descritas.

2. Implementar los mecanismos necesarios para garantizar la encapsulación del ADT. Implementar una función auxiliar (privada) validar, que compruebe que un conjunto no tiene elementos repetidos.

3. Implementar las operaciones heredadas de Object: equals, toString, hashCode.

4. Implementar un método main donde se haga una prueba unitaria de cada una de las operaciones: Unión, diferencia, intersección, diferencia simétrica e equals. En sus pruebas unitarias verificar que el resultado es correcto y validar que el conjunto no tenga elementos repetidos.

## Notas: 
1. Utilizar listas simplemente enlazadas para la representación de los conjuntos. No usar estructuras predefinidas en los lenguajes (e.g. ArrayList, LinkedList, [], etc.)
2. Quienes trabajan el Python no pueden utilizar tipos genéricos, pero si pueden utilizar anotaciones de tipo.

