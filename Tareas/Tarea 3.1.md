# Tarea 3.1 Ejercicios AFN

## a) El lenguaje donde toda cadena tiene exactamente dos 'b's:

Explicación: Cualquier cadena en este lenguaje debe tener exactamente dos 'b's, con cualquier cantidad de 'a's antes, entre y después de las 'b's.

* Expresión regular: (a∗ba∗ba∗)

* Diagrama de transición: 


Estado inicial --> q0

Estado final --> q2

q0 --a--> q0

q0 --b--> q1

q1 --a--> q1

q1 --b--> q2

q2 --a--> q2

q2 --b--> q2

## b) El lenguaje de las cadenas no vacías, donde toda 'a' está entre dos 'b's:

Explicación: En este lenguaje, todas las cadenas no vacías deben tener al menos una 'a' y esta 'a' debe estar entre dos 'b's.

* Expresión regular: (b+a(b+a)∗b+)

* Diagrama de transición:

Estado inicial --> q0

Estado final --> q2

q0 --a--> q0

q0 --b--> q1

q1 --a--> q2

q1 --b--> q1

q2 --a--> q2

q2 --b--> q1

## c) El lenguaje donde toda cadena contiene el sufijo 'aba':

Explicación: Cada cadena en este lenguaje debe terminar con 'aba'.

* Expresión regular: (a∗ba∗ba)

* Diagrama de transición:

Estado inicial --> q0

Estado final --> q3

q0 --a--> q1

q0 --b--> q0

q1 --a--> q3

q1 --b--> q2

q2 --a--> q1

q2 --b--> q0

q3 --a--> q3

q3 --b--> q3

## d) El lenguaje donde ninguna cadena contiene las subcadenas 'aa' ni 'bb':

Explicación: En este lenguaje, ninguna cadena puede tener 'aa' ni 'bb' como subcadena.

* Expresión regular: ((a∣b)∗)∗
 
* Diagrama de transición:

Estado inicial y final --> q0

q0 --a--> q1

q0 --b--> q2

q1 --a--> q3

q1 --b--> q2

q2 --a--> q1

q2 --b--> q4

q3 --a--> q3

q3 --b--> q2

q4 --a--> q1

q4 --b--> q4

## e) El lenguaje donde toda cadena contiene la subcadena 'baba':

Explicación: Cada cadena en este lenguaje debe contener la subcadena 'baba'.

* Expresión regular: (a∣b)∗baba(a∣b) ∗
 
* Diagrama de transición:

Estado inicial --> q0

Estado final --> q3

q0 --a--> q0

q0 --b--> q1

q1 --a--> q2

q1 --b--> q1

q2 --a--> q3

q2 --b--> q1

q3 --a--> q3

q3 --b--> q3

## f) El lenguaje donde toda cadena contiene por separado a las cadenas 'ab' y 'ba':

Explicación: En este lenguaje, cada cadena debe contener tanto 'ab' como 'ba' por separado.

* Expresión regular: ((ab)∣(ba))(a∣b)∗
 
* Diagrama de transición:

Estado inicial --> q0

Estado final --> q2

q0 --a--> q1

q0 --b--> q3

q1 --a--> q1

q1 --b--> q2

q2 --a--> q1

q2 --b--> q2

q3 --a--> q3

q3 --b--> q4

q4 --a--> q1

q4 --b--> q4

## g) Toda cadena es de longitud impar y contiene una cantidad par de 'a's:

Explicación: En este lenguaje, todas las cadenas deben tener una longitud impar y una cantidad par de 'a's.

* Expresión regular: b∗(ab∗ab∗)∗
 
* Diagrama de transición:

Estado inicial --> q0

Estado final --> q1

q0 --a--> q2

q0 --b--> q0

q1 --a--> q0

q1 --b--> q3

q2 --a--> q1

q2 --b--> q2

q3 --a--> q2

q3 --b--> q3
