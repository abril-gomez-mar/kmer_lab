## Interacción 1
Modo: ASK

Pregunta: ¿De qué forma puedo introducir un salto de línea, con tal de que los mensajes mostrados en en la pantalla no estén amontonados?

Aprendí: Basta con añadir '\n' al final de cada f-string.


## Interacción 2
Modo: ASK

Pregunta: Si en un renglón imprimo la secuencia original de ADN introducida por el usuario, ¿cómo puedo indicar que, por cada ciclo adentro del for, deseo que se coloque el signo '^' debajo de cada letra presente en el kmer actual?

Aprendí: Puedo usar una cadena de texto que combine espacios en blanco (los caracteres ajenos al kmer en uso) y repeticiones del símbolo '^'. Por consiguiente, puedo declarar una variable, *linea*, que sea un string conformado por la suma de dos multiplicaciones: ' ' * i (los caracteres no pertenecientes al kmer actualizado) y '^' * k (denota la cantidad de nucleótidos englobados por el kmer). Entonces, puedo ocupar esta línea de código:

```python
linea = ' ' * i + '^' * k

```
